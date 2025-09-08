from scholarly import scholarly, ProxyGenerator
import json
from datetime import datetime
import os
from collections import defaultdict
import time, random

# ---------- Proxy setting ----------
pg = ProxyGenerator()
use_proxy = False

try:
    if pg.FreeProxies():
        scholarly.use_proxy(pg)
        print("Trying free proxy...")
        # Test the availability of proxy
        try:
            _ = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
            use_proxy = True
            print("Free proxy works, using it.")
        except Exception as e:
            print(f"Free proxy test failed: {e}")
except Exception as e:
    print(f"Setting up free proxy failed: {e}")

if not use_proxy:
    print("Using runner IP (no proxy).")

# ---------- Fetch author ----------
author_id = os.environ['GOOGLE_SCHOLAR_ID']

for attempt in range(3):
    try:
        print(f"Start fetching author: {datetime.now()}")
        author = scholarly.search_author_id(author_id)
        scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
        print(f"Finished fetching author: {datetime.now()}")
        break
    except Exception as e:
        print(f"Attempt {attempt+1} failed: {e}")
        if attempt < 2:  # Do not delay after the final attempt
            delay = random.uniform(2, 10)  # Random 2-10 sec
            print(f"Waiting {delay:.1f} seconds before retrying...")
            time.sleep(delay)
        else:
            raise RuntimeError(f"Failed after 3 attempts: {e}")

# ---------- Processing author data ----------
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']: v for v in author['publications']}
os.makedirs('results', exist_ok=True)

# Save author info
with open('results/gs_data.json', 'w', encoding='utf-8') as f:
    json.dump(author, f, ensure_ascii=False, indent=2)

# total_citation / h-index / i10-index / total_publication
with open('results/gs_data_total_citation.json', 'w', encoding='utf-8') as f:
    json.dump({
        "schemaVersion": 1,
        "label": "citations",
        "message": str(author.get('citedby', 0))
    }, f, ensure_ascii=False, indent=2)

with open('results/gs_data_h_index.json', 'w', encoding='utf-8') as f:
    json.dump({
        "schemaVersion": 1,
        "label": "h-index",
        "message": str(author.get('hindex', 0))
    }, f, ensure_ascii=False, indent=2)

with open('results/gs_data_i10_index.json', 'w', encoding='utf-8') as f:
    json.dump({
        "schemaVersion": 1,
        "label": "i10-index",
        "message": str(author.get('i10index', 0))
    }, f, ensure_ascii=False, indent=2)

with open('results/gs_data_total_publications.json', 'w', encoding='utf-8') as f:
    json.dump({
        "schemaVersion": 1,
        "label": "total-publications",
        "message": str(len(author['publications']))
    }, f, ensure_ascii=False, indent=2)

print("Data fetching and processing complete.")