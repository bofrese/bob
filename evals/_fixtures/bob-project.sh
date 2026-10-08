#!/usr/bin/env bash
# Smallest project that looks like it uses bob (triggers the SessionStart primer and the hub description).
set -e
mkdir -p docs/process docs/domain projects/x src
echo "# Done criteria" > docs/process/done-criteria.md
echo "# Domain" > docs/domain/README.md
echo "# Kanban" > projects/x/_kanban.md
printf 'def total(items):\n    return sum(i.price for i in items)\n' > src/cart.py
