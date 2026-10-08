# Files to create or update

## Dockerfile
- Use an appropriate official base image for the stack.
- Install all dependencies needed for development AND testing.
- Don't copy source code into the image - it will be mounted.
- Include any tooling needed for development (linters, test runners, debug tools).
- Set up a working directory that matches the mount point.
- Handle initial setup steps (database init, migrations) as an entrypoint or init script that runs on first start.

## docker-compose.yml (if needed)
- Use when the project requires supporting services (database, cache, queue, etc.).
- Mount source code as a volume.
- Map ports sensibly - avoid conflicts with common local services.
- Use .env file for configuration where appropriate.
- Include healthchecks for services the app depends on.

## Makefile
Respect existing Makefile conventions if one exists. Add or update targets to provide a standard interface:

```makefile
# Standard targets - adapt to the project's actual needs:
make setup      # First-time setup: build images, install deps, init DB, seed data
make build      # Build/rebuild containers or application
make run        # Start the dev environment (docker-compose up or docker run)
make stop       # Stop the dev environment
make test       # Run the test suite inside the container
make shell      # Open a shell inside the running container
make logs       # Tail container logs
make clean      # Remove containers, volumes, generated files
make reset      # Full reset: clean + setup (nuclear option)
```

Only include targets that make sense for the project. Don't add `make deploy` if there's no deployment pipeline. Don't add `make install` if it's not meaningful.

Each target should:
- Have a brief help comment
- Work on macOS, Linux, and Windows (via Make for Windows or WSL)
- Be idempotent where possible (running it twice doesn't break things)

If no Makefile exists, create one. If one exists, integrate new targets while preserving existing conventions.

## .dockerignore
Create or update to exclude:
- `.git/`, `node_modules/`, `__pycache__/`, build artifacts
- Anything that shouldn't be in the Docker context

## Install documentation
Update `INSTALL.md` if the project has one; otherwise create or update `docs/install.md`:

```
# Installation & Development Setup

## Prerequisites
What needs to be installed on the host machine (Docker, Make, etc.).

## Quick Start
Step-by-step from clone to running system. Should be short.

## Makefile Commands
Table of available make targets and what they do.

## Architecture
Brief overview of the Docker setup - what containers run, what's mounted, what's persisted.

## Configuration
Environment variables, config files, how to customize.

## Troubleshooting
Common issues and how to resolve them.
```
