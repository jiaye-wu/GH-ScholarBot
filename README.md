# GH-ScholarBot: Google Scholar Crawler for GitHub Pages

A Google Scholar Crawler for GitHub Pages decoupled from [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io) jekyll theme, with **added features** of *i10-index* and *h-index* caching, and **improved usability**.

## About the crawler

This distribution of Google Scholar crawler is originally extracted from [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io) theme and now maintined by [me](https://github.com/jiaye-wu). It works well with [Academic Pages](https://github.com/academicpages/academicpages.github.io), [al-folio](https://github.com/alshedivat/al-folio), and [multi-language-al-folio](https://github.com/george-gca/multi-language-al-folio) (personally tested).

My modifications to the original version are adding the cached data for *i10-index* and *h-index* individually so that one can easily cite the data without digging through `gs_data.json`.

The benefits of this cawler version include:

1. **cached data**: avoid querying Google Scholar too frequently to encounter HTTP error code 429 "too many requests" which slows down local website building and stops GitHub Pages auto-deployment.
2. **optimized access**: use CDN (in `_config.yml` set `google_scholar_stats_use_cdn` to `true`) to have better GS data access to in special Internet enviroments with censorship and delay. CDN also avoids `domain blocked` error from GitHub.com when there are too many refreshes. 
3. **easy deployment**: fork, fill in your info, and play.

## Appearance preview

**Total citation:** <a href='https://scholar.google.com/citations?user=D2n8tswAAAAAJ'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fjiaye-wu%2FGH-ScholarBot@google-scholar-stats%2Fgs_data_total_citation.json&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>

**Total publications:** <a href='https://scholar.google.com/citations?user=D2n8tswAAAAAJ'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fjiaye-wu%2FGH-ScholarBot@google-scholar-stats%2Fgs_data_total_publications.json&labelColor=f6f6f6&color=9cf&style=flat&label=publications"></a>

**h-index:** <a href='https://scholar.google.com/citations?user=D2n8tswAAAAAJ'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fjiaye-wu%2FGH-ScholarBot@google-scholar-stats%2Fgs_data_h_index.json&labelColor=f6f6f6&color=9cf&style=flat&label=h-index"></a>

**i10-index:** <a href='https://scholar.google.com/citations?user=D2n8tswAAAAAJ'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fjiaye-wu%2FGH-ScholarBot@google-scholar-stats%2Fgs_data_i10_index.json&labelColor=f6f6f6&color=9cf&style=flat&label=i10-index"></a>

## Auto-fetch

Your Google Scholar data is automatically fetched at UTC 2:42 every Sunday.

**Note:** It is pretty normal to be blocked by Google several times a week resulting in a build action failure, even if random proxies are used. A success once a week should be sufficient for personal use. To change the frequency of the scheduled action, please refer to [google_scholar_crawler.yaml](https://github.com/jiaye-wu/GH-ScholarBot/blob/main/.github/workflows/google_scholar_crawler.yaml). This scheduled task can also be run **on demand** manually, by visiting the Actions page > Get Citation Data > (Re)Run workflow.

**The most recent fetch:** [![Get Citation Data](https://github.com/jiaye-wu/GH-ScholarBot/actions/workflows/google_scholar_crawler.yaml/badge.svg?branch=main)](https://github.com/jiaye-wu/GH-ScholarBot/actions/workflows/google_scholar_crawler.yaml)

## Implementation

### Option 1: installation inside website

You can **merge** this repo with (inside) your GitHub Pages website:

1. download this repo, keep the folder structure and paste the files into your website root folder;
2. setup `_config.yml`: copy the lines in this project and change the contents to be yours;
3. in **project settings** > **Actions** > **General** > **Workflow permissions**, grant **Read and write permissions**;
4. in **project settings** > **Secret and variables** > **Actions** > **Repository Secrets** > creat a key name `GOOGLE_SCHOLAR_ID` with value being *the string after your Google Scholar profile url* `user=`;
5. the crawler will create a **branch** in the **website** project named `google-scholar-stats` with 4 json files: `gs_data.json` (full data for all your papers), `gs_data_h_index.json`, `gs_data_i10_index.json`, and `gs_data_total_citation.json`. 
6. If the crawler fails to do so, you can manually create a **branch** name `google-scholar-stats` from `main`. The content in this `google-scholar-stats` branch will be permanantly cleared and replaced by the `json` files when the crawler is working.

### Option 1: Display your Google Scholar Badge

To use it **in your `.md` file** for your website pages:

**To change in the following codes:** `<your-github-user-name>` and `GOOGLE_SCHOLAR_ID`

#### For **Google Scholar citation badge**

Use CDN for GitHub (delays in data-refresh might exist):

```
<a href='https://scholar.google.com/citations?user=GOOGLE_SCHOLAR_ID'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2F<your-github-user-name>%2F<your-github-user-name>.github.io@google-scholar-stats%2Fgs_data_total_citation.json&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>
```

Use GitHub.com:

```
<a href='https://scholar.google.com/citations?user=GOOGLE_SCHOLAR_ID'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fgithub.com%2F<your-github-user-name>%2F<your-github-user-name>.github.io@google-scholar-stats%2Fgs_data_total_citation.json&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>
```

#### For **Google Scholar publication badge**

Use CDN for GitHub (delays in data-refresh might exist):

```
<a href='https://scholar.google.com/citations?user=GOOGLE_SCHOLAR_ID'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2F<your-github-user-name>%2F<your-github-user-name>.github.io@google-scholar-stats%2Fgs_data_total_publications.json&labelColor=f6f6f6&color=9cf&style=flat&label=publications"></a>
```

Use GitHub.com:

```
<a href='https://scholar.google.com/citations?user=GOOGLE_SCHOLAR_ID'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fgithub.com%2F<your-github-user-name>%2F<your-github-user-name>.github.io@google-scholar-stats%2Fgs_data_total_publications.json&labelColor=f6f6f6&color=9cf&style=flat&label=publications"></a>
```

#### For **Google Scholar h-index badge** 

Use CDN for GitHub (delays in data-refresh might exist):

```
<a href='https://scholar.google.com/citations?user=GOOGLE_SCHOLAR_ID'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2F<your-github-user-name>%2F<your-github-user-name>.github.io@google-scholar-stats%2Fgs_data_h_index.json&labelColor=f6f6f6&color=9cf&style=flat&label=h-index"></a>
```

Use GitHub.com:

```
<a href='https://scholar.google.com/citations?user=GOOGLE_SCHOLAR_ID'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fgithub.com%2F<your-github-user-name>%2F<your-github-user-name>.github.io@google-scholar-stats%2Fgs_data_h_index.json&labelColor=f6f6f6&color=9cf&style=flat&label=h-index"></a>
```

#### For **Google Scholar i10-index badge** 

Use CDN for GitHub (delays in data-refresh might exist):

```
<a href='https://scholar.google.com/citations?user=GOOGLE_SCHOLAR_ID'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2F<your-github-user-name>%2F<your-github-user-name>.github.io@google-scholar-stats%2Fgs_data_i10index.json&labelColor=f6f6f6&color=9cf&style=flat&label=i10-index"></a>
```

Use GitHub.com:

```
<a href='https://scholar.google.com/citations?user=GOOGLE_SCHOLAR_ID'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fgithub.com%2F<your-github-user-name>%2F<your-github-user-name>.github.io@google-scholar-stats%2Fgs_data_i10index.json&labelColor=f6f6f6&color=9cf&style=flat&label=i10-index"></a>
```

### Option 2: Standalone installation

You can **fork** this repo into your own GitHub account, for example `github.com/<your-github-user-name>/GH-ScholarBot/`

1. setup `_config.yml`: change the contents to be yours;
2. in **project settings** > **Actions** > **General** > **Workflow permissions**, grant **Read and write permissions**;
3. in **project settings** > **Secret and variables** > **Actions** > **Repository Secrets** > creat a key name `GOOGLE_SCHOLAR_ID` with value being *the string after your Google Scholar profile url* `user=`;
4. the crawler will create a **branch** in the **crawler** project named `google-scholar-stats` with 4 json files: `gs_data.json` (full data for all your papers), `gs_data_h_index.json`, `gs_data_i10_index.json`, and `gs_data_total_citation.json`. 
5. If the crawler fails to do so, you can manually create a **branch** name `google-scholar-stats` from `main`. The content in this `google-scholar-stats` branch will be permanantly cleared and replaced by the `json` files when the crawler is working.

### Option 2: Display your Google Scholar Citation Badge

To use it **in your `.md` file** for your website pages:

**To change in the following codes:** `<your-github-user-name>` and `GOOGLE_SCHOLAR_ID`

**Note:** the codes below is different from **Option 1**. It uses data under `github.com/<your-github-user-name>/GH-ScholarBot/` other than `github.com/<your-github-user-name>/<your-github-user-name>.github.io/`.

#### For **Google Scholar citation badge** 

Use CDN for GitHub (delays in data-refresh might exist):

```
<a href='https://scholar.google.com/citations?user=GOOGLE_SCHOLAR_ID'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2F<your-github-user-name>%2FGH-ScholarBot@google-scholar-stats%2Fgs_data_total_citation.json&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>
```

Use GitHub.com:

```
<a href='https://scholar.google.com/citations?user=GOOGLE_SCHOLAR_ID'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fgithub.com%2F<your-github-user-name>%2FGH-ScholarBot@google-scholar-stats%2Fgs_data_total_citation.json&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>
```

#### For **Google Scholar h-index badge** 

Use CDN for GitHub (delays in data-refresh might exist):

```
<a href='https://scholar.google.com/citations?user=GOOGLE_SCHOLAR_ID'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2F<your-github-user-name>%2FGH-ScholarBot@google-scholar-stats%2Fgs_data_h_index.json&labelColor=f6f6f6&color=9cf&style=flat&label=h-index"></a>
```

Use GitHub.com:

```
<a href='https://scholar.google.com/citations?user=GOOGLE_SCHOLAR_ID'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fgithub.com%2F<your-github-user-name>%2FGH-ScholarBot@google-scholar-stats%2Fgs_data_h_index.json&labelColor=f6f6f6&color=9cf&style=flat&label=h-index"></a>
```

#### For **Google Scholar i10-index badge** 

Use CDN for GitHub (delays in data-refresh might exist):

```
<a href='https://scholar.google.com/citations?user=GOOGLE_SCHOLAR_ID'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2F<your-github-user-name>%2FGH-ScholarBot@google-scholar-stats%2Fgs_data_i10index.json&labelColor=f6f6f6&color=9cf&style=flat&label=i10-index"></a>
```

Use GitHub.com:

```
<a href='https://scholar.google.com/citations?user=GOOGLE_SCHOLAR_ID'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fgithub.com%2F<your-github-user-name>%2FGH-ScholarBot@google-scholar-stats%2Fgs_data_i10index.json&labelColor=f6f6f6&color=9cf&style=flat&label=i10-index"></a>
```

## All your other citation data for each paper

Available in `gs_data.json`. You can be creative and do whatever you want with it!
