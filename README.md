# GH-ScholarBot: Google Scholar Crawler for GitHub Pages

A Google Scholar Crawler for GitHub Pages decoupled from [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io) jekyll theme, with **added features** of *i10-index* and *h-index* caching, and **improved usability**.

## About the crawler

This distribution of Google Scholar crawler is originally extracted from [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io) theme and now maintined by [me](https://github.com/jiaye-wu). It works well with [Academic Pages](https://github.com/academicpages/academicpages.github.io), [al-folio](https://github.com/alshedivat/al-folio), and [multi-language-al-folio](https://github.com/george-gca/multi-language-al-folio) (personally tested).

My modifications to the original version are adding the cached data for *i10-index* and *h-index* individually so that one can easily cite the data without digging through ```gs_data.json```.

The benefits of the crawler include:

1. **cached data**: avoid querying Google Scholar too frequently to encounter HTTP error code 429 "too many requests" which slows down local website building and stops GitHub Pages auto-deployment.
2. **optimized access**: use CDN to have better GS data access in special Internet enviroment like in China.

## Implementation

To try to implement it on your website:

1. keep the folder structure and paste the files into your website root folder;
2. setup ```_config.yml```: copy the lines in this project and change the contents to be yours;
3. in **project settings** > **Actions** > **General** > **Workflow permissions**, grant **Read and write permissions**;
4. in **project settings** > **Secret and variables** > **Actions** > **Repository Secrets** > creat a key name ```GOOGLE_SCHOLAR_ID``` with value being *the string after your Google Scholar profile url* ```user=```;
5. the crawler will create a **branch** in the website project named ```google-scholar-stats``` with 4 json files: ```gs_data.json``` (full data for all your papers), ```gs_data_hindex.json```, ```gs_data_i10.json```, and ```gs_data_shieldsio.json```. 
6. If the crawler fails to do so, you can manually create a **branch** name ```google-scholar-stats``` from ```master```. The content in **this branch** will be permanantly cleared when the crawler is working.

## Display your Google Scholar Citation Badge

To use it **in your ```.md``` file** for your website pages:

### For **Google Scholar citation badge** 

- Use ```<a href='https://scholar.google.com/citations?user=GOOGLE_SCHOLAR_ID'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2F<your-github-user-name>%2F<your-github-user-name>.github.io@google-scholar-stats%2Fgs_data_shieldsio.json&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>```.
- Example appearance <a href='https://scholar.google.com/citations?user=D2n8tswAAAAAJ'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fjiaye-wu%2FGH-ScholarBot@google-scholar-stats%2Fgs_data_shieldsio.json&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>.

### For **Google Scholar h-index badge** 

- Use ```<a href='https://scholar.google.com/citations?user=GOOGLE_SCHOLAR_ID'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2F<your-github-user-name>%2F<your-github-user-name>.github.io@google-scholar-stats%2Fgs_data_hindex.json&labelColor=f6f6f6&color=9cf&style=flat&label=h-index"></a>```.
- Example appearance <a href='https://scholar.google.com/citations?user=D2n8tswAAAAAJ'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fjiaye-wu%2FGH-ScholarBot@google-scholar-stats%2Fgs_data_hindex.json&labelColor=f6f6f6&color=9cf&style=flat&label=h-index"></a>.

### For **Google Scholar i10-index badge** 

- Use ```<a href='https://scholar.google.com/citations?user=GOOGLE_SCHOLAR_ID'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2F<your-github-user-name>%2F<your-github-user-name>.github.io@google-scholar-stats%2Fgs_data_i10index.json&labelColor=f6f6f6&color=9cf&style=flat&label=i10-index"></a>```.
- Example appearance <a href='https://scholar.google.com/citations?user=D2n8tswAAAAAJ'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fjiaye-wu%2FGH-ScholarBot@google-scholar-stats%2Fgs_data_i10.json&labelColor=f6f6f6&color=9cf&style=flat&label=i10-index"></a>.

### All your other citation data for each paper

Available in ```gs_data.json```. You can be creative and do whatever you want with it!
