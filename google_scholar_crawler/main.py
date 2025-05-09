from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os

pg = ProxyGenerator()
success = pg.FreeProxies()  # 使用免费代理池（成功率较低）
# success = pg.ScraperAPI('YOUR_API_KEY')  # 或用付费API（如 scraperapi.com）
scholarly.use_proxy(pg)

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