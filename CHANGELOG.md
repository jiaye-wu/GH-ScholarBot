# Changelog

All notable changes to this project are documented in this file.

## [6.0] - 2026-08-13

### Major changes

- Consolidated the direct and proxy crawlers into a single `main.py` entry point.
- Fixed direct mode so it no longer calls `scholarly.use_proxy(None)`, which can unexpectedly start free-proxy discovery.
- Added a reliable fallback chain: **Get Citation Data (with free proxy)** automatically triggers **Get Citation Data (without free proxy fallback)** after any failed proxy run, including a manually triggered run.
- Added **Test Free Proxy**, a manual-only diagnostic workflow that verifies free-proxy availability without writing JSON files, pushing data, or triggering a fallback.
- Added workflow concurrency protection and modernized Actions setup with `actions/checkout@v4`, `actions/setup-python@v5`, Python 3.12, and pip caching.
- Improved crawler resilience with explicit `GOOGLE_SCHOLAR_ID` validation, incremental retry backoff, clearer error logging, atomic JSON writes, and safer publication-ID handling.
- Bounded Scholar request retries and timeouts, added an 8-minute isolated-process watchdog for direct access, added unbuffered workflow logs, and capped data-fetch runs at 45 minutes to prevent blocked requests from consuming the GitHub Actions six-hour job limit.
- Reused the successful proxy-test lookup during a normal proxy crawl to avoid an unnecessary Google Scholar request.

### Compatibility

- Existing JSON filenames and badge schemas are unchanged.
- The `updated` value in `gs_data.json` now uses a timezone-aware UTC ISO 8601 timestamp.

## [5.0] - 2025-11-02

Major changes:

1. Add workflows with and without proxy (see [Actions](https://github.com/jiaye-wu/GH-ScholarBot/actions) page) and allow for manual execution.
2. Updated instructions in `README.md` about the possible solutions to Google blocking the crawler.

**Full Changelog**: https://github.com/jiaye-wu/GH-ScholarBot/compare/4.0...5.0

## [4.0] - 2025-09-08

Major changes:

1. Add total_publications functionality;
2. Update auto-fetch logic: 3 attempts on free proxy, if it fails, fall back to runner IP;
3. Update auto-fetch time from 02:00 to 02:42, avoid time-number-based blocking.

**Full Changelog**: https://github.com/jiaye-wu/GH-ScholarBot/compare/3.0...4.0

## [3.0] - 2025-04-25

Major changes:

1. Bumped up versions for pip packages;
2. Enable free proxies to obtain data to reduce the chance of being blocked.

**Full Changelog**: https://github.com/jiaye-wu/GH-ScholarBot/compare/2.0...3.0

## [2.0] - 2025-02-14

Major update. New features include:

- Allow standalone implementation.
- Clean up unnecessary entries.
- Options to show badges with and without using CDN.
- Rename GS data JSON files to be clearer.
- Allow refresh of data on-demand.
- Disable unnecessary workflow.

**Full Changelog**: https://github.com/jiaye-wu/GH-ScholarBot/compare/1.0...2.0

## [1.0] - 2025-02-14

First release
