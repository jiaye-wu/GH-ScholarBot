from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os

# Try to use free proxy
use_proxy = False
pg = ProxyGenerator()
try:
    if pg.FreeProxies():  # Free proxy successful.
        scholarly.use_proxy(pg)
        try:
            scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
            use_proxy = True
            print("Free proxy works, using it.")
        except Exception as e:
            print(f"Free proxy failed on request: {e}")
except Exception as e:
    print(f"Free proxy setup failed: {e}")

if not use_proxy:
    print("Falling back to runner IP (no proxy).")

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

citation_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_total_citation.json', 'w') as outfile:
    json.dump(citation_data, outfile, ensure_ascii=False)

hindex_data = {
  "schemaVersion": 1,
  "label": "h-index",
  "message": f"{author['hindex']}",
}
with open(f'results/gs_data_h_index.json', 'w') as outfile:
    json.dump(hindex_data, outfile, ensure_ascii=False)

i10_data = {
  "schemaVersion": 1,
  "label": "i10-index",
  "message": f"{author['i10index']}",
}
with open(f'results/gs_data_i10_index.json', 'w') as outfile:
    json.dump(i10_data, outfile, ensure_ascii=False)

total_pubs = len(author['publications'])
print(f"Total publications: {total_pubs}")
pub_count_data = {
    "schemaVersion": 1,
    "label": "total-publications",
    "message": f"{total_pubs}",
}
with open(f'results/gs_data_total_publications.json', 'w', encoding='utf-8') as outfile:
    json.dump(pub_count_data, outfile, ensure_ascii=False)