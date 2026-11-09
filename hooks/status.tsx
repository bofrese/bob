import { atom, read, update } from 'claude-code'
import type { EngineInterface, Register } from 'claude-code'

import type { Loaded } from '../types'

const PANE = 'bob-knowledge'
const HUB = 'bob'
const last = atom({ plugin: 'bob', key: 'last' } as const, null)
const story = atom({ plugin: 'bob', key: 'story' } as const, null)
const loaded = atom({ plugin: 'bob', key: 'loaded' } as const, [], {
  shape: 'loaded-1',
})

const HEADINGS: Record<Loaded['kind'], string> = {
  skill: 'Skills',
  bob: 'bob references',
  project: 'Project docs',
  other: 'Other markdown',
}

async function showStatus($: EngineInterface) {
  const skill = await read($, last)
  const id = await read($, story)
  const count = (await read($, loaded)).length
  const label = [skill, id].filter(part => part !== null).join(' · ')
  $.ui.status(label === '' ? undefined : `bob: ${label} (${count} loaded, /bob-knowledge)`)
}

function remember($: EngineInterface, entry: Loaded) {
  return update($, loaded, list =>
    list.some(one => one.label === entry.label) ? list : [...list, entry],
  )
}

function certainStory(stdout: string): string | undefined {
  try {
    const found: { certain?: boolean; candidates?: { story_id?: string }[] } = JSON.parse(stdout)
    return found.certain === true && found.candidates?.length === 1
      ? found.candidates[0]?.story_id
      : undefined
  } catch {
    // --selftest and other modes print no JSON.
    return undefined
  }
}

export const register: Register = on => {
  // Learned from the first bob skill's path, so reads of bob's own reference
  // files can be told apart from project docs.
  let bobRoot: string | undefined

  on('session.start', async ($, e, next) => {
    await $.command.register({
      name: 'bob-knowledge',
      description: 'Show or hide the bob skills and docs loaded this session',
    })
    await showStatus($)

    return next(e)
  })

  on('command.run', { command: 'bob-knowledge' }, async $ => {
    if ((await $.ui.panes()).some(pane => pane.id === PANE)) {
      await $.ui.close({ id: PANE })
      return { text: 'bob knowledge pane closed.' }
    }
    await $.ui.open({ id: PANE, title: 'bob knowledge', closeOnEscape: true })

    return { text: 'bob knowledge pane opened.' }
  })

  on('skill.prompt', async ($, e, next) => {
    const isBob = e.pluginName === 'bob' || e.skill.startsWith('bob:')
    if (!isBob) {
      return next(e)
    }
    const name = e.skill.replace(/^bob:/, '')
    if (e.path !== undefined && bobRoot === undefined) {
      bobRoot = e.path.slice(0, e.path.lastIndexOf('/skills/') + 1)
    }
    await remember($, { kind: 'skill', label: name })
    // Every phase skill loads the hub; showing the hub would hide the phase.
    if (name !== HUB) {
      await update($, last, () => name)
    }
    await showStatus($)

    return next(e)
  })

  // The main story is the one story.py last resolved with certainty
  // (references/story.md resolves again after a confirmation or a switch).
  // Work routed to other stories never runs story.py, so it cannot move it.
  on('tool.call', { tool: 'Bash' }, async ($, e, next) => {
    const ran = await next(e)
    if (ran.deny !== undefined || ran.isError === true || !e.command.includes('story.py')) {
      return ran
    }
    const id = certainStory(ran.result.stdout)
    if (id !== undefined) {
      await update($, story, () => id)
      await showStatus($)
    }

    return ran
  })

  on('tool.call', { tool: 'Read' }, async ($, e, next) => {
    const ran = await next(e)
    if (ran.deny !== undefined || ran.isError === true || !e.file_path.endsWith('.md')) {
      return ran
    }
    const root = (await $.session.root()) + '/'
    const path = e.file_path
    const entry: Loaded =
      bobRoot !== undefined && path.startsWith(bobRoot)
        ? { kind: 'bob', label: path.slice(bobRoot.length) }
        : path.startsWith(root)
          ? { kind: 'project', label: path.slice(root.length) }
          : { kind: 'other', label: path }
    await remember($, entry)
    await showStatus($)

    return ran
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    const { Box, Text } = $.ui.resolve(e)
    const list = await read($, loaded)
    const skill = await read($, last)
    const id = await read($, story)
    const kinds = (Object.keys(HEADINGS) as Loaded['kind'][]).filter(kind =>
      list.some(one => one.kind === kind),
    )

    return (
      <Box flexDirection="column">
        <Text bold>Last skill: {skill ?? 'none yet'}</Text>
        <Text bold>Story: {id ?? 'none'}</Text>
        {list.length === 0 && <Text dimColor>Nothing loaded yet.</Text>}
        {kinds.map(kind => (
          <Box key={kind} flexDirection="column" marginTop={1}>
            <Text bold>{HEADINGS[kind]}</Text>
            {list
              .filter(one => one.kind === kind)
              .map(one => (
                <Text dimColor>  {one.label}</Text>
              ))}
          </Box>
        ))}
      </Box>
    )
  })
}
