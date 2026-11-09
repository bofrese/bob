import { expect, test } from 'claude-code/testing'

const PANE = {
  plugin: 'bob',
  component: 'Pane',
  requestId: 'bob-knowledge',
  surface: 'terminal',
  props: {
    title: 'bob knowledge',
    isFocused: false,
    bodyColumns: 60,
    placement: 'dock',
    scroll: { offset: 0, bodyRows: 20 },
    view: {},
  },
} as const

const CERTAIN = JSON.stringify({ tier: 'id', certain: true, candidates: [{ story_id: 'BOB-12' }] })
const OPEN = JSON.stringify({ tier: 'open', certain: false, candidates: [{ story_id: 'BOB-9' }] })

test('the pane shows the last phase, the main story and what was read', async ($, on) => {
  on('command.register', () => ({ value: { command: 'bob-knowledge' } }))
  on('session.start', (_, e) => ({ cwd: e.cwd }))
  on('session.root', () => ({ value: '/proj' }))
  on('skill.prompt', (_, e) => ({ text: e.text }))
  // Stands for story.py: the request text decides which result it prints.
  on('tool.call', (_, e) =>
    e.tool === 'Bash'
      ? { result: { stdout: e.command.includes('open') ? OPEN : CERTAIN, stderr: '', interrupted: false } }
      : { result: {} },
  )

  await $.session.start({ cwd: '/proj', surface: 'terminal', isInteractive: true })
  await $.skill.prompt({ skill: 'bob:plan', text: '', pluginName: 'bob', path: '/p/bob/skills/plan/SKILL.md' })
  // The hub loads after the phase and must not replace it.
  await $.skill.prompt({ skill: 'bob:bob', text: '', pluginName: 'bob', path: '/p/bob/skills/bob/SKILL.md' })
  await $.tool.call({ tool: 'Read', file_path: '/p/bob/skills/bob/references/done.md' })
  await $.tool.call({ tool: 'Read', file_path: '/proj/docs/guidelines/x.md' })
  await $.tool.call({ tool: 'Read', file_path: '/proj/src/a.ts' })
  await $.tool.call({ tool: 'Bash', command: 'python3 story.py "plan BOB-12"' })
  // Neither routed work in another story nor an unconfirmed guess moves it.
  await $.tool.call({ tool: 'Write', file_path: '/proj/projects/core/stories/BOB-14/_index.md', content: '' })
  await $.tool.call({ tool: 'Bash', command: 'python3 story.py "open"' })

  const ui = await $.ui.mount(PANE)
  expect((await ui.find({ type: 'Text', text: /Last skill/ }))?.text).toBe('Last skill: plan')
  expect(await ui.find({ type: 'Text', text: /skills\/bob\/references\/done\.md/ })).toBeTruthy()
  expect((await ui.find({ type: 'Text', text: /Story/ }))?.text).toBe('Story: BOB-12')
  expect(await ui.find({ type: 'Text', text: /docs\/guidelines\/x\.md/ })).toBeTruthy()
  expect(await ui.find({ type: 'Text', text: /a\.ts/ })).toBeFalsy()
  await ui.unmount()
})
