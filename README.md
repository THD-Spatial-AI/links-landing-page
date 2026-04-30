# LinkHub

A central platform for publishing permanent landing pages for conferences, events, and research projects.
Each page is defined by a single `page.json` file and deployed automatically to GitHub Pages.

**Documentation:** [LinkHub-Docs](https://thd-spatial-ai.github.io/linkhub/docs/)

## Quick start

1. Create a new folder named after your event slug (e.g. `egu-2027/`)
2. Add a `page.json` file inside it — copy from `_template/page.json`
3. Fill in the event name, title, links, and institution
4. Commit to `main` — the page is live within ~60 seconds

Full guide: [docs/add-a-page.md](docs/add-a-page.md)

## Repository structure

```
/
├── egu-2026/           ← example event page
│   └── page.json
├── _template/
│   └── page.json       ← copy this for each new page
├── scripts/
│   └── generate.py     ← converts page.json files to HTML
├── docs/               ← MkDocs documentation source
├── mkdocs.yml
├── requirements.txt
└── .github/workflows/
    └── deploy.yml      ← builds and deploys on every push to main
```

> [!IMPORTANT]
> In the repository **Settings → Pages**, set the source to **GitHub Actions**.
>
> - This allows the deploy workflow to publish the generated pages to GitHub Pages.
>
> - This only needs to be done once by the repo owner.

## Local preview

```bash
python3 scripts/generate.py   # writes to _site/
python3 -m http.server 8080 --directory _site
# open http://localhost:8080
```

## License

[MIT License](LICENSE)
