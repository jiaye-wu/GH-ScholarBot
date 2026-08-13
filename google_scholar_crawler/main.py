import argparse
import json
import os
import random
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

from scholarly import ProxyGenerator, scholarly


MAX_ATTEMPTS = 3
RETRY_DELAYS_SECONDS = (15, 45)
RESULTS_DIR = Path("results")


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def get_author_id() -> str:
    author_id = os.environ.get("GOOGLE_SCHOLAR_ID")
    if not author_id:
        raise RuntimeError("GOOGLE_SCHOLAR_ID is not configured.")
    return author_id


def configure_free_proxy(author_id: str):
    """Configure and test a free proxy, or fail so the fallback workflow runs."""
    proxy_generator = ProxyGenerator()
    try:
        if not proxy_generator.FreeProxies():
            raise RuntimeError("No working free proxy was found.")
        scholarly.use_proxy(proxy_generator)
        print("Testing free proxy...")
        author = scholarly.search_author_id(author_id)
        print("Free proxy works, using it.")
        return author
    except Exception as exc:
        raise RuntimeError(f"Free proxy setup or test failed: {exc}") from exc


def fetch_author(author_id: str, initial_author=None):
    author = initial_author
    for attempt in range(MAX_ATTEMPTS):
        try:
            print(f"Fetching author (attempt {attempt + 1}/{MAX_ATTEMPTS}): {now()}")
            if author is None:
                author = scholarly.search_author_id(author_id)
            scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
            print(f"Finished fetching author: {now()}")
            return author
        except Exception as exc:
            author = None
            print(f"Attempt {attempt + 1} failed ({type(exc).__name__}): {exc}")
            if attempt == MAX_ATTEMPTS - 1:
                raise RuntimeError(f"Failed after {MAX_ATTEMPTS} attempts.") from exc
            delay = RETRY_DELAYS_SECONDS[attempt] + random.uniform(0, 10)
            print(f"Waiting {delay:.1f} seconds before retrying...")
            time.sleep(delay)


def write_json_atomically(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False
    ) as temporary_file:
        json.dump(value, temporary_file, ensure_ascii=False, indent=2)
        temporary_name = temporary_file.name
    os.replace(temporary_name, path)


def save_results(author: dict) -> None:
    publications = author.get("publications", [])
    publication_map = {}
    missing_ids = 0
    duplicate_ids = 0
    for publication in publications:
        publication_id = publication.get("author_pub_id")
        if not publication_id:
            missing_ids += 1
        elif publication_id in publication_map:
            duplicate_ids += 1
        else:
            publication_map[publication_id] = publication
    if missing_ids or duplicate_ids:
        print(f"Publication IDs skipped: missing={missing_ids}, duplicate={duplicate_ids}.")

    author["updated"] = now()
    author["publications"] = publication_map
    write_json_atomically(RESULTS_DIR / "gs_data.json", author)

    badges = {
        "gs_data_total_citation.json": ("citations", author.get("citedby", 0)),
        "gs_data_h_index.json": ("h-index", author.get("hindex", 0)),
        "gs_data_i10_index.json": ("i10-index", author.get("i10index", 0)),
        "gs_data_total_publications.json": ("total-publications", len(publication_map)),
    }
    for filename, (label, value) in badges.items():
        write_json_atomically(
            RESULTS_DIR / filename,
            {"schemaVersion": 1, "label": label, "message": str(value)},
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch Google Scholar author data.")
    parser.add_argument(
        "--use-free-proxy",
        action="store_true",
        help="Require a tested free proxy; exit non-zero when none is available.",
    )
    args = parser.parse_args()
    author_id = get_author_id()

    initial_author = None
    if args.use_free_proxy:
        initial_author = configure_free_proxy(author_id)
    else:
        print("Using runner IP (no proxy).")

    save_results(fetch_author(author_id, initial_author))
    print("Data fetching and processing complete.")


if __name__ == "__main__":
    main()
