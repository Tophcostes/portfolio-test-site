# Portfolio Test Site

A personal portfolio website for Christopher Costes — designer of experiences, services, and strategies. Built as a static, dependency-free site using plain HTML, CSS, and a small amount of vanilla JavaScript.

## Overview

The site showcases case studies, publications, and experiments. It's intentionally lightweight: no build step, no framework, no package manager. You can open `index.html` directly in a browser or serve the folder with any static file server.

## Features

- **Responsive layout** that adapts from mobile to desktop with a collapsible nav menu
- **Automatic dark mode** via `prefers-color-scheme`
- **Staggered fade-in animations** on card grids
- **Static & portable** — no build tools, no dependencies, no server required
- **Inter** font loaded from Google Fonts

## Pages

| Page | Description |
| --- | --- |
| `index.html` | Landing page with intro and a featured-work grid |
| `work.html` | Full list of professional case studies |
| `work-*.html` | Individual case study pages (JP Morgan, The League, Lyft OTTO, Ontra, Remark, ComplianceAI, Embedded Banking, Academic Coaching) |
| `anecdotes.html` | Index of side projects and experiments |
| `anecdotes-*.html` | Individual experiment write-ups |
| `publications.html` | List of writing and published work |
| `bio.html` | Background and biography |

## Project Structure

```
.
├── index.html              # Landing page
├── work.html               # Work index
├── work-*.html             # Case study pages
├── anecdotes.html          # Experiments index
├── anecdotes-*.html        # Experiment pages
├── publications.html       # Publications
├── bio.html                # Bio
└── assets/
    ├── styles.css          # All site styles (CSS variables, dark mode, layout)
    └── main.js             # Mobile menu toggle + fade-in animations
```

## Running Locally

Because the site is fully static, any of the following will work:

**Open directly in a browser**
```sh
open index.html
```

**Or serve with Python**
```sh
python3 -m http.server 8000
```
Then visit <http://localhost:8000>.

**Or serve with Node**
```sh
npx serve .
```

## Customizing

- **Colors, spacing, and typography** are defined as CSS variables at the top of `assets/styles.css` (`:root` and the `prefers-color-scheme: dark` block).
- **Navigation links** live in the `<nav>` block at the top of each HTML page.
- **Featured work cards** on the landing page are in `index.html` under the `#work` section.

## Tech

- HTML5
- CSS3 (custom properties, grid, flexbox, media queries)
- Vanilla JavaScript (no dependencies)
- Inter via Google Fonts

## Contact

- Email: christophercostes@gmail.com
- LinkedIn: <https://www.linkedin.com/in/christophercostes/>
- Medium: <https://christophercostes.medium.com>

## License

All rights reserved. Content and case studies are © Christopher Costes.
