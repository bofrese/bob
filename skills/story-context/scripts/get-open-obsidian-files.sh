#!/bin/bash
# Returns vault-relative paths of all open markdown tabs in Obsidian
obsidian eval code="app.workspace.getLeavesOfType('markdown').map(l => l.view?.file?.path).filter(Boolean).join('\n')" 2>/dev/null | sed 's/^=> //'
