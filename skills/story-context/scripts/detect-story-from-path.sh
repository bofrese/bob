#!/bin/bash
# Usage: ./detect-story-from-path.sh <file-path>
# Outputs SUBPROJECT, STORY_ID, and optionally TASK_ID if path is within a story folder
path="$1"
if [[ "$path" =~ projects/([^/]+)/stories/([A-Z]+-[0-9]+) ]]; then
    echo "SUBPROJECT=${BASH_REMATCH[1]}"
    echo "STORY_ID=${BASH_REMATCH[2]}"
    if [[ "$path" =~ /tasks/([^/]+) ]]; then
        echo "TASK_ID=${BASH_REMATCH[1]}"
    fi
fi
