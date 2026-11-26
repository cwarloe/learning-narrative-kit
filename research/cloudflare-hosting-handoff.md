# Cloudflare hosting migration handoff

Updated 2026-11-26. Scope: `cwarloe/learning-narrative-kit`, including `/portland-desk/`. This is **prepared, not deployed**. Preserve the current GitHub Pages publication until a new Cloudflare URL has been tested in a browser.

## Site shape and verified package

- The source of public files is the repository's already-generated `docs/` tree. Do not generate from `examples/` at deploy time. Existing chapter authoring and validation stay unchanged.
- Cloudflare Workers Static Assets can publish `docs/` directly; no server code, database, or secrets in the site are needed. Repo source stays on GitHub; only delivery moves.
- `npm run cloudflare:dry-run` completed successfully with `cf@1.0.0-rc.6` on 2026-11-26 against GitHub `main` `fc7db9d`: 285 asset entries, including `index.html`, `portland-desk/index.html`, `portland-desk/assets/lnk-terminal.js` and the source video. Generated `.cloudflare/` output is ignored. The largest single asset is the existing ~4.46 MB episode video.
- The deployed Worker name is derived from `package.json`: `learning-narrative-kit`, unless a future explicit configuration overrides it. Confirm this name is not already assigned to another project before deploying.

## Deployment and cutover (not yet performed)

1. Restore authenticated Cloudflare access and **list existing Workers and Pages projects** in Charles's account. Reuse an appropriate existing project if one already hosts this content; do not create duplicates. The Cloudflare connector read account identity and account ID, but Pages listing repeatedly returned a fresh authorization request, and the browser dashboard required sign-in. Do not extract a credential or claim permission success from these incomplete reads.
2. Verify source content with `python tools/check_hub_links.py --strict` and the existing `.github/workflows/validate.yml` checks. Run `npm run cloudflare:dry-run`. Avoid editing generated `docs/` merely to change hosting.
3. With a properly authorized Cloudflare `cf` session or `CLOUDFLARE_API_TOKEN` environment, run `npm run cloudflare:deploy` from the repository root. This creates an assets-only Worker. Cloudflare documentation also supports connecting GitHub to Workers Builds so pushes to `main` deploy automatically; prefer that once the correct Cloudflare project is known and GitHub access is authorized. Never commit a token.
4. Verify the returned `workers.dev` or custom URL, in a browser at desktop and Android widths: homepage, `/portland-desk/`, episode navigation, Docsify CDN-loaded content, glossary, recorded terminal and video, all assets. Check 404 handling and internal links. A dry-run alone does not prove live hosting.
5. Only after full Cloudflare verification, update canonical links and any Pages-specific README/AGENTS wording via a separate reviewed change. Disable GitHub Pages *after* users have a working Cloudflare address. No custom domain has been selected for this kit, so do not create or modify DNS records automatically.

## Known scope boundaries

- Harrowmere's private living-workplace V1 and V2 previews are separate **Sites** projects; neither is this public Learning Narrative Kit courseware deployment. Do not deploy over them or make them public.
- Other GitHub Pages candidates (e.g. `cwarloe/daily-bible-reading`) need their own inventory and content-update verification, especially nightly jobs. Do not reuse this static deployment blindly for a scheduled reader.
- Current GitHub Pages fallback remains `https://cwarloe.github.io/learning-narrative-kit/portland-desk/`; no Cloudflare live URL has been obtained. Cloudflare Worker may be named differently if an existing project is reused.

## Official references

- [Deploy a static assets directory with `cf`](https://developers.cloudflare.com/cf/projects/#deploy-a-static-assets-directory)
- [Workers Static Assets](https://developers.cloudflare.com/workers/static-assets/index.md)
- [Workers Builds Git integration](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/)
