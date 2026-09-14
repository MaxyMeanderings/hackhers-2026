#!/usr/bin/env bash
# Build a notes-free static bundle and publish it to the workshop Railway service.
set -euo pipefail
slides_dir=$(cd "$(dirname "$0")/.." && pwd)
cd "$slides_dir"
package_dir=$(mktemp -d "${TMPDIR:-/tmp}/hackherthon-slides-publish.XXXXXX")
./node_modules/.bin/slidev build --without-notes --base / --out "$package_dir/site"
cp hosting/Caddyfile hosting/Dockerfile hosting/railway.json "$package_dir/"
# Export a current PDF before publishing if the slide source has changed.
[ -f workshop.pdf ] || { echo 'Export workshop.pdf first.' >&2; exit 1; }
[ ! slides.md -nt workshop.pdf ] || { echo 'slides.md is newer than workshop.pdf. Re-export the PDF first.' >&2; exit 1; }
cp workshop.pdf "$package_dir/site/workshop.pdf"
railway up "$package_dir" --path-as-root \
  --project 39b4e941-7267-474e-b007-8a21d8bf4f3d \
  --environment 99820221-2d4a-4307-95ad-cff347136276 \
  --service 2954d400-44ca-4927-b3ca-342054f783bd --detach
printf 'Deployment submitted. Retained bundle: %s\n' "$package_dir"
printf '%s\n' 'Check deployment status before sharing: https://slides-production-06e4.up.railway.app'
