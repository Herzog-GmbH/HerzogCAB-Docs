# Herzog CAB - User Manual (Source)

This is the source repository for the **Herzog CAB** user manual.
The rendered site is automatically published to GitHub Pages.

> **Live:** https://herzog-gmbh.github.io/HerzogCAB-Docs/

## Quick start for authors

```cmd
REM 1) Python 3.11+ installed? If not: https://www.python.org/downloads/
python --version

REM 2) Virtual environment + dependencies
cd docs-site
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

REM 3) Local preview server (live reload on changes)
mkdocs serve

REM   -> open http://127.0.0.1:8000 in your browser
```

## Project structure

```
docs-site/
├── mkdocs.yml              # central configuration & navigation
├── requirements.txt        # Python dependencies
├── docs/                   # >>> Content lives here <<<
│   ├── index.md            # landing page
│   ├── assets/             # logos, images, downloads
│   ├── installation/       # chapter "Installation"
│   ├── erste-schritte/     # chapter "Getting Started"
│   ├── stammdaten/         # ...
│   └── ...
└── .github/
    └── workflows/
        └── docs.yml        # automatic build & deploy
```

> Folder names under `docs/` are kept in German (e.g. `erste-schritte`,
> `stammdaten`) because they form the URL slugs and were the original
> structure. Display labels in the sidebar are translated in `mkdocs.yml`.

## Writing content

* Every page is a Markdown file (`.md`) under `docs/`.
* The order in the sidebar is set in `mkdocs.yml` under `nav:`.
* Images / screenshots go into `docs/assets/screenshots/<chapter>/...`
  and are embedded with `![Description](../assets/screenshots/...)`.

## Conventions

* **Voice:** end customer who operates Herzog CAB on the shop floor.
  No code-level terms (e.g. `QSettings`, `JSON`) in body text.
* **Formatting:** buttons in **bold** (e.g. **Save**), menu paths with
  `>` (e.g. *File > Settings*).
* **Callouts:** use admonition blocks for warnings, tips and notes:

  ```markdown
  !!! tip "Tip"
      If the workspace is on a network share, ...

  !!! warning "Caution"
      When moving the workspace, all users must sign in again.

  !!! info "Note"
      This feature is available from version 1.3 onwards.
  ```

## Publishing

Push to `main` -> GitHub Actions builds the site -> deploy to `gh-pages`.
Nothing to do manually.

## Contact

Questions about the docs: e.siemering@herzog-online.com
