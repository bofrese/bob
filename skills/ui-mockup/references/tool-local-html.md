# Tool: local HTML files

Each mockup is a self-contained HTML file in the repository. Use it when no Claude Design type is available, when the user wants no remote tool, or for web pages where real HTML and CSS are close to the product.

## Layout

```text
docs/design/{name}/
  README.md
  source/{Artboard}.html    one file per artboard, inline CSS, fixed size (for example 390x844 for a phone)
  source/gallery.html       all artboards side by side, with titles
  screens/{Artboard}.png
```

Each file sets its size on the outer element and has a `<title>` that says what it shows. Shared styles go into one `source/tokens.css`, linked from each file, so the design system section of the spec has one source.

## The five steps

1. **Create**: write `source/{Artboard}.html`. Add it to `gallery.html` (a list of names, widths and titles at the top of its script).
2. **Sync**: git is the sync. Nothing to download.
3. **Preview**: `python3 -m http.server 8765 --directory docs/design/{name}/source`, then open `http://localhost:8765/gallery.html` or a single file. Each file also opens from disk, unless it loads other files.
4. **Screenshot**: with Playwright, open each artboard at its own size and save `screens/{Artboard}.png`. Look at the result before you show it to the user.
5. **Publish** (optional, to share or comment): publish `source/` as an artifact with the Artifact tool, or commit and let the user open the files. The repository copy stays the source.

## Gallery

The gallery shows every artboard with no parameters. A query parameter that selects some artboards is optional. Each artboard is an `iframe` at its own size with its title above it, so the user can compare them side by side.
