export type Loaded = { kind: 'skill' | 'bob' | 'project' | 'other'; label: string }

declare module 'claude-code' {
  interface PluginState {
    'bob': { last: string | null; story: string | null; loaded: Shaped<Loaded[]> }
  }
}
