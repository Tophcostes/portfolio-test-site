# Portfolio Test Site

A personal portfolio website for Christopher Costes — designer of experiences, services, and strategies. Built as a static, dependency-free site using plain HTML, CSS, and vanilla JavaScript. Mirrors the live site at [christophercostes.com](https://christophercostes.com).

## Overview

The site showcases professional case studies, experiments, publications, and a bio. It's intentionally lightweight: no build step, no framework, no package manager. All images are stored locally — no CDN or network dependency at runtime.

## Features

- **Responsive layout** that adapts from mobile to desktop with a collapsible nav menu
- **Automatic dark mode** via `prefers-color-scheme`
- **Staggered fade-in animations** on card grids
- **Locally hosted images** — all assets downloaded from the live site into `assets/images/`
- **Static & portable** — works offline, no server required
- **Inter** font loaded from Google Fonts (only external dependency)

## Pages

| Page | Description |
| --- | --- |
| `index.html` | Landing page with intro and 4 featured work cards |
| `work.html` | Full index of 7 professional case studies |
| `work-embeddedbanking.html` | JP Morgan & Chase — Tools for Embedded Banking |
| `work-theleague.html` | The League — Building a better dating service |
| `work-lyftotto.html` | Lyft OTTO — Creating Trust in A.I. (VoiceUI) |
| `work-ontra.html` | Ontra — Dashboard design for Legal Tech |
| `work-complianceai.html` | Compliance.ai — Digital Library Design |
| `work-remark.html` | REMARK — Real Estate Redesign |
| `work-academic-coaching.html` | CMU's Academic Coaching — Rebrand |
| `anecdotes.html` | Index of 10 side projects and experiments |
| `anecdotes-mycelium-connections.html` | Motion Design: Complexity of Mycelium |
| `anecdotes-thegoodmeal.html` | Design Research: Stewards of the Land |
| `anecdotes-plastic-world.html` | Design Future: Artifacts from a Plastic Future |
| `anecdotes-physical-design.html` | Design Study: Physical Prototypes |
| `anecdotes-laundry-machine-ui.html` | Physical Interfaces: Laundry Machine UI |
| `anecdotes-project-four-7xwwe.html` | McKinsey Case Competition |
| `anecdotes-metaphor-animation.html` | Motion Design: Lost Without Metaphor |
| `anecdotes-post-series.html` | Design Study: 30 Days of Poster Remixes |
| `anecdotes-magic-thinking.html` | Design Research: Magic Thinking |
| `anecdotes-fake-news-visualization.html` | Design Research: Misinformation Giga Map |
| `publications.html` | List of writing and published work |
| `bio.html` | Background and biography |

## Project Structure

```
.
├── index.html
├── work.html
├── work-*.html                     # 7 case study pages
├── anecdotes.html
├── anecdotes-*.html                # 10 experiment pages
├── publications.html
├── bio.html
└── assets/
    ├── styles.css                  # All styles: CSS variables, dark mode, layout, components
    ├── main.js                     # Mobile menu toggle + fade-in animations
    └── images/
        ├── home/                   # Index page card thumbnails
        ├── work-thumbnails/        # Work index card thumbnails
        ├── work-embeddedbanking/   # JP Morgan case study images
        ├── work-theleague/         # The League case study images (29 assets)
        ├── work-lyftotto/          # Lyft OTTO case study images + GIFs (49 assets)
        ├── work-ontra/             # Ontra case study images
        ├── work-complianceai/      # Compliance.ai case study images
        ├── work-remark/            # REMARK case study images
        ├── work-academic-coaching/ # Academic Coaching case study images
        ├── anecdotes-thumbnails/   # Anecdotes index card thumbnails
        ├── anecdotes-mycelium/
        ├── anecdotes-thegoodmeal/
        ├── anecdotes-plastic-world/
        ├── anecdotes-physical-design/
        ├── anecdotes-mckinsey/
        ├── anecdotes-post-series/  # 21 poster images
        ├── anecdotes-magic-thinking/
        ├── anecdotes-fake-news/
        ├── bio/                    # Headshot and secondary photo
        └── publications/
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

- **Colors, spacing, and typography** — CSS variables at the top of `assets/styles.css` (`:root` and `prefers-color-scheme: dark` blocks)
- **Navigation links** — `<nav>` block at the top of each HTML file
- **Featured work cards** — `index.html` under `#work`
- **Case study images** — swap files in the relevant `assets/images/work-{slug}/` directory; filenames are referenced directly in the HTML

## CSS Components

| Class | Purpose |
| --- | --- |
| `.case-study-hero-image` | Full-width banner at top of case study pages |
| `.case-study-image` | Single image with border + rounded corners |
| `.case-study-image-grid.cols-2/3/4` | Responsive image grid (collapses to 1 col on mobile) |
| `.case-study-section-banner` | Section header graphic |
| `.card-img` | Thumbnail container on index/list pages (4:3, `object-fit: cover`) |

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

All rights reserved. Content, case studies, and images are © Christopher Costes.
