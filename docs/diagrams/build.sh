#!/bin/sh
# Portable rebuild: does not start the application or database.
set -eu
cd "$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
for tool in pdflatex pdftocairo; do
    command -v "$tool" >/dev/null 2>&1 || { printf '%s\n' "Missing tool: $tool" >&2; exit 1; }
done
build_dir=$(mktemp -d "./.diagram-build.XXXXXX")
trap 'rm -rf "$build_dir"' EXIT HUP INT TERM
for name in system-architecture data-ingestion api-requests genre-releases rating-updates; do
    if ! pdflatex -halt-on-error -interaction=nonstopmode -no-shell-escape \
        -output-directory="$build_dir" "$name.tex" >"$build_dir/$name.stdout" 2>&1; then
        cat "$build_dir/$name.stdout" >&2
        exit 1
    fi
    cp "$build_dir/$name.pdf" "$name.pdf"
    pdftocairo -svg "$name.pdf" "$name.svg"
    printf '%s\n' "Built $name.pdf and $name.svg"
done
