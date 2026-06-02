#!/bin/bash
# Reads paths from stdin, outputs only those within a projects/*/stories/ID/ structure
grep -E 'projects/[^/]+/stories/[A-Z]+-[0-9]+/'
