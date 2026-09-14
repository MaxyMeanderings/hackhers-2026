# Shared workshop slides

Public URL: https://slides-production-06e4.up.railway.app
PDF: https://slides-production-06e4.up.railway.app/workshop.pdf

Railway project: `hack-her-thon-slides` (`39b4e941-7267-474e-b007-8a21d8bf4f3d`).
Service: `slides` (`2954d400-44ca-4927-b3ca-342054f783bd`).
Environment: `production` (`99820221-2d4a-4307-95ad-cff347136276`).

This is public link access, without a login. Caddy serves a prebuilt static deck;
there is no model runtime or API key in the deployment. Speaker notes are excluded
using Slidev's `--without-notes` build flag. Only the static output and current PDF
are uploaded, not the repository, instructor guide or development files.

## Publish later edits

Export a current PDF using the slides project's documented export command first.
From the slides directory, run `mise exec node@24.13.1 -- bash hosting/publish.sh`.
Implementation: [publish.sh:1](publish.sh). This rebuilds the static site and uploads
it to the existing service; it does not enable GitHub autodeploy.

Check the Railway deployment result and open a direct slide link such as `/19`.
The final-slide prompt, template and playbook links use this same public host.
The PDF is also directly available at `/workshop.pdf`.

Runtime configuration: [Caddyfile](Caddyfile), [Dockerfile](Dockerfile),
[railway.json](railway.json). Railway terminates HTTPS and routes to port 8080.
Source: https://docs.railway.com/guides/caddy .

Initial deployment: `aeaef412-8dff-4b2f-a9bb-d260e40641b9`.
