# Architecture and flow diagrams

Five title-free vector figures for repository documentation and slides. Each
has an editable TikZ `.tex` source, a one-page `.pdf`, and an `.svg` rendered by
Poppler. `diagram-style.tex` shares the white canvas, black text, flat light-blue
nodes and Beamer blue (RGB 51, 51, 178).

| Stem | Scope |
| --- | --- |
| `system-architecture` | MovieLens CSVs → MongoDB → Flask → browser |
| `data-ingestion` | Read inputs, clean/aggregate, write movie and rating data |
| `api-requests` | JavaScript request, Flask database query, JSON chart data |
| `genre-releases` | Filter year, expand genre memberships, count and sort |
| `rating-updates` | Validate, save the current vote, update the movie summary |

## Scope and source

These are conceptual success-path summaries of `load_data.py`, `app.py` and
`static/dashboard.js`, not a schema inventory or deployment claim. Architecture
arrow labels name the connecting operation; the figure reads left to right as
the data-to-chart path, not network-request direction. The 1995 filter is an
example, not a measured result.

The checked-in loader aggregates the source ratings and retains a baseline
sample in `ratings`. The current rating endpoint writes `ratings` and `movies`
separately. The figures show these logical operations, not full raw retention
or multi-document transaction guarantees.

## Rebuild

Requires `pdflatex` with `standalone.cls`, TikZ and Latin Modern, plus Poppler's
`pdftocairo`; no dependency installation or application run is needed.

```sh
sh docs/diagrams/build.sh  # from the repository root
```

The script also works from another working directory, rebuilding all five
PDF/SVG pairs. Build scratch files are created beside the sources and removed
on exit. Refresh slide assets manually from this folder **only when** the
presentation asset folder already exists:

```sh
if [ -d ../../presentation/assets/diagrams ]; then
  cp system-architecture.pdf data-ingestion.pdf rating-updates.pdf \
    ../../presentation/assets/diagrams/
fi
```
