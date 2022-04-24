This repository contains the full source for the final paper of INF 312 (Winter 2022), taught by Rohan Alexander.

## File Structure
### `/` (root)
- `paper_5.rmd`: A standalone R Markdown script that runs all of the required code to prepare and format the paper via `knitr`.
- `LICENSE`: A copy of the Do What The Fuck You Want To Public License (WTFPL), which fully liberates you to view, modify, and replicate the contents of this repository as desired.
- `README.md`: This file.
- `datasheet.md`: An enhanced data information sheet, based on [Gebru et al](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t8QB).

### `in/`
- `references.bib`: All references to R packages and literature used in the paper, in BibTeX format. It is automatically consumed by `paper_5.rmd` to generate a references list in APA format, along with in-text citations.
- `corpus/`: The three English wordlists of consideration in the paper. Each has been left as-is, save for the modifications of ensuring that they were in lexical order and consisted of only lowercase Latin letters.
  - `linux.txt`: The dictionary found in `/usr/share/dict/words` on Ubuntu distributions. This particular file was attained from a Xubuntu distribution running Ubuntu 21.10 (`impish`).
  - `collins.txt`: The Harper Collins wordlist, in particular that in use in the Collins divisions of North American competitive Scrabble play.
  - `NWL2020.txt`: The [NASPA](https://scrabbleplayers.org/w/Welcome_to_NASPAWiki) (North American Scrabble Association) official Scrabble wordlist, used in the majority of English-language competitive Scrabble play outside of Collins divisions. This wordlist supplanted the 2018 edition on [January 6, 2021](https://www.scrabbleplayers.org/w/NWL2020), with the majority of changes surrounding the removal of "offensive terms of abuse" toward protected characteristics.
  <br>**NOTE**: Unlike the other two corpora, `NWL2020.txt` is sorted by length, and then lexicographically. However, owing to the specific properties of the word pairs in question, this difference in ordering still upholds the in-place lexicographical properties assumed in the paper.

- `cache`: Calculating word pairs that satisfy the requisite properties is asymptotically quadratic over each corpus. Determining these pairs in R, even only if once per corpus, was untenably slow. As a result, an ad-hoc Python script (`scripts/find_pairs.py`, below) was written to process each corpus and batch-write found pairs to CSV files. As a result, the R environment in the final paper need only read these CSVs, instead of handling the extensive computation every time the session restarted.
    - `linux.csv`, `collins.csv`, `NWL202.csv`: The respective cached lists of word pairs for the three corpora of study. The properties of these files are explored in greater detail in the **Data** section of the paper.
    - `corpus_splits.csv`: An ad-hoc, script-generated file consisting of words from every wordlist, dissected into each of their successive two-character substrings. For example, the first word in the list, "aardvark" (from the `linux` corpus) has rows for "aa", "ar", "rd", "dv", "va", "ar", and "rk". Similar to the corpus cache files, this file was generated to turn an extremely expensive computation into a one-time operation (until the script is re-run).

### `scripts/`
- `scratch.rmd`: The very earliest explorations of corpus data, divided into notebook-like chunks of R code. As in previous assignments, even exploratory scripts are not excluded from the repository, as they may belie interesting jumping-off points for future research. Code is free; ideas are expensive.
- `exploration.rmd`: Continued ad-hoc explorations of corpus data, including experimental versions of the final tables/visualizations that appear in the paper. An effort was taken to heavily annotate code with its purpose, results, and any questions it left me with.
- `find_pairs.py`: A command-line based Python script which, when fed a wordlist of the appropriate format, automatically filters out unacceptable words (by length, presence of diacritics, etc.) and compares them pairwise to look for pairs satisfying the Split Decisions property. These properties are introduced in-depth in the **Introduction** section.

### `out/`
- `paper_5.pdf`: The most recently-generated PDF edition of the final paper, including all text, tables, graphs, and cross-references. 