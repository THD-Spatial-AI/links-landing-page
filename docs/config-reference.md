# Config reference

Every landing page is defined by a single `page.json` file inside its own folder. This page describes every field you can use.

---

## Top-level fields

| Field | Required | Description |
|---|---|---|
| `event` | Yes | The conference or event name, shown as a badge above the title. Example: `"EGU General Assembly 2026"` |
| `title` | Yes | The project or presentation title. Use `×` (the multiplication sign) to get an amber-coloured separator. Example: `"BuEM × EnerPlanET"` |
| `subtitle` | Yes | One sentence describing the project. Shown in muted text below the title. |
| `links` | Yes | A list of link cards. Must contain at least one item. |
| `institutions` | No | A list of institution names shown in the footer. |

---

## Link fields (`links` array)

Each item in `links` becomes one card on the page.

| Field | Required | Description |
|---|---|---|
| `category` | Yes | A short label shown above a group of cards. Cards with the same category are grouped together. Example: `"Source Code"`, `"Web App"`, `"Dataset"` |
| `title` | Yes | The card heading. Example: `"EnerPlanET App"` |
| `url` | Yes | The full URL the card links to. Must start with `https://`. |
| `description` | No | One sentence shown in smaller text below the title. |
| `icon` | No | Icon name (see table below). Defaults to `link` if omitted. |

### Available icons

| Icon name | Best used for |
|---|---|
| `globe` | Web apps, live tools |
| `code` | Source code, scripts |
| `github` | GitHub repositories |
| `table` | Data tables, spreadsheets |
| `document` | Papers, reports, PDFs |
| `paper` | Preprints, publications |
| `data` | Datasets, databases |
| `map` | Maps, geospatial tools |
| `tool` | CLI tools, utilities |
| `link` | General links (default) |

---

## Institution fields (`institutions` array)

Each item in `institutions` becomes one line in the page footer.

| Field | Required | Description |
|---|---|---|
| `name` | Yes | Department, institute, or faculty name. |
| `unit` | No | University or organisation name, shown below the department. |

---

## Full example

```json
{
  "event": "EGU General Assembly 2026",
  "title": "BuEM × EnerPlanET",
  "subtitle": "Integrating a building energy model with a regional planning tool for energy community analysis.",
  "links": [
    {
      "category": "Planning Tool",
      "title": "EnerPlanET App",
      "url": "https://enerplanet.th-deg.de/",
      "description": "Regional planning tool for energy community analysis and scenario modelling",
      "icon": "globe"
    },
    {
      "category": "Source Code",
      "title": "BuEM",
      "url": "https://github.com/SomadSahoo/buem",
      "description": "Building Energy Model — source code and documentation",
      "icon": "code"
    },
    {
      "category": "Source Code",
      "title": "city2tabula",
      "url": "https://github.com/THD-Spatial-AI/city2tabula",
      "description": "City data processing tool — generates TABULA-compatible building typology inputs",
      "icon": "table"
    }
  ],
  "institutions": [
    {
      "name": "Copernicus Institute of Sustainable Development",
      "unit": "Utrecht University"
    },
    {
      "name": "Faculty of Applied Informatics",
      "unit": "Technische Hochschule Deggendorf (THD)"
    }
  ]
}
```

---

## Common mistakes

**Invalid JSON** — JSON is strict about formatting. Common errors:

- Missing comma between items in a list
- Trailing comma after the last item (not allowed in JSON)
- Using single quotes `'` instead of double quotes `"`

If the build fails after you save your file, go to the **Actions** tab on GitHub to see the error message. It will tell you which line has the problem.

**Wrong URL format** — Every URL must begin with `https://`. A URL without the protocol will not work:

```json
"url": "example.com"          ← wrong
"url": "https://example.com"  ← correct
```

**Slug with spaces or uppercase** — The folder name becomes part of the URL. Use only lowercase letters, numbers, and hyphens.
