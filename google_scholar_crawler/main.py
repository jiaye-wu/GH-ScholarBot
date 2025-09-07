from scholarly import scholarly, ProxyGenerator
import json
from datetime import datetime
import os
from collections import defaultdict
import time, random

# ---------- 代理设置 ----------
pg = ProxyGenerator()
use_proxy = False

try:
    if pg.FreeProxies():
        scholarly.use_proxy(pg)
        print("Trying free proxy...")
        # 测试代理是否可用
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

# ---------- 抓取 author ----------
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
        if attempt < 2:  # 最后一次不延迟
            delay = random.uniform(2, 10)  # 随机 2–10 秒
            print(f"Waiting {delay:.1f} seconds before retrying...")
            time.sleep(delay)
        else:
            raise RuntimeError(f"Failed after 3 attempts: {e}")

# ---------- 处理 author 数据 ----------
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']: v for v in author['publications']}
os.makedirs('results', exist_ok=True)

# 保存完整 author 信息
with open('results/gs_data.json', 'w', encoding='utf-8') as f:
    json.dump(author, f, ensure_ascii=False, indent=2)

# 总引用 / h-index / i10-index
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

# ---------- 按年份统计文章数和引用数 ----------
pubs_per_year = defaultdict(int)
citations_per_year = defaultdict(int)

for pub in author['publications'].values():
    year = pub.get('pub_year') or pub['bib'].get('year')
    if year is None:
        continue
    try:
        year = int(year)
    except ValueError:
        continue
    pubs_per_year[year] += 1
    citations = pub.get('num_citations', 0)
    citations_per_year[year] += citations

pubs_per_year = dict(sorted(pubs_per_year.items()))
citations_per_year = dict(sorted(citations_per_year.items()))

with open('results/gs_data_per_year.json', 'w', encoding='utf-8') as f:
    json.dump({
        "publications_per_year": pubs_per_year,
        "citations_per_year": citations_per_year
    }, f, ensure_ascii=False, indent=2)

print("Data fetching and processing complete.")
