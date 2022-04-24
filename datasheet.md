1. *For what purpose was the dataset created? Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description.*
    - The corpora were created as English wordlists; essentially, a reference for what does and does not constitute and "English word" for various purposes. In particular:
    - The `linux` dataset, which was sourced from `/usr/share/dict/words` on a standard Ubuntu distribution, serves as a baseline for many word-based functions of the GNU+Linux operating system, such as spell check and word prediction. 
    - Conversely, the `collins` and `NWL2020` datasets are primarily used for the study and officiation of English-language competitive Scrabble. Players are entitled in certain circumstances to challenge the validity of an opponent's word, at which point they can refer to the designated wordlist of the tournament to see if the word is found.
2. *Who created the dataset (for example, which team, research group) and on behalf of which entity (for example, company, institution, organization)?*
    - The `linux` dataset has been curated over the development of the Ubuntu operating system by the open-source community.
    - The `collins` dataset is created and published by HarperCollins, LLC. as a commercial work. It is made available to the Scrabble community via Hasbro, who holds to the Scrabble mark in the United States and Canada.
    - The `NWL2020` dataset is curated by the Dictionary Committee of the North American Scrabble Players Association (NASPA) for use in NASPA tournaments. In particular, the modification of the previous NWL2018 into the present version was spearheaded by NASPA CEO and DC chair John Chew.

**Composition**

1. *What do the instances that comprise the dataset represent (for example, documents, photos, people, countries)? Are there multiple types of instances (for example, movies, users, and ratings; people and interactions between them; nodes and edges)? Please provide a description.*
	- English words, comprised of lower-case Latin characters (potentially with diacritics), with one word on each line.
2. *How many instances are there in total (of each type, if appropriate)?*
	- `linux.txt` consists of 102774 words.
    - `collins.txt` consists of 279496 words.
    - `NWL2020.txt` consists of 191852 words.
    - Total: 574122 words.
3. *Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set? If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set (for example, geographic coverage)? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (for example, to cover a more diverse range of instances, because instances were withheld or unavailable).*
	- "English words" is an undefineable category, for a variety of reasons. As a result, these wordlists do not portend to contain *every possible* English utterance, but rather such a list that is useful for its respective purpose (spell check, Scrabble, etc.) Similarly, these corpora may contain a number of words that prescriptivist English speakers may not agree with their categorization as words, for any number of inane reasons.
    - Each of these corpora consists of a different subset of English words; the inclusion or omission of any given word is largely arbitrary, or subject to concerns of computational or size expense. However, as previously noted, the `nwl` corpus in particular has recently had several words removed, in particular pejorative slurs. As a direct example, the "N-word" appears in the `linux` and `collins` corpora, but not `nwl`.
    - Although English words are bounded below in length ("I", "a"...) and unbounded above ("ultraultraultraultra...violet"), each corpus has its own bounds for length of its entries. Notably, the two Scrabble-oriented wordlists have no one-letter words, as Scrabble does not permit these as valid plays.
4. *What data does each instance consist of? "Raw" data (for example, unprocessed text or images) or features? In either case, please provide a description.*
	- Text. On the machine used to write this paper, the text consisted of UTF-8 encoded text with Unix line endings; however, this may differ on different operating systems.
5. *Is there a label or target associated with each instance? If so, please provide a description.*
	- N/A
6. *Is any information missing from individual instances? If so, please provide a description, explaining why this information is missing (for example, because it was unavailable). This does not include intentionally removed information, but might include, for example, redacted text.*
	- N/A
7. *Are relationships between individual instances made explicit (for example, users' movie ratings, social network links)? If so, please describe how these relationships are made explicit.*
	- No. Each entry appears once and only once in its respective corpus.
8. *Are there recommended data splits (for example, training, development/validation, testing)? If so, please provide a description of these splits, explaining the rationale behind them.*
	- The confines of the Split Decisions word puzzle necessitate dividing the words of each corpora by length (i.e., number of letters). Although this was simply handled using conditionals in the Python script used to discover word pairs, there may be motivating reasons for pre-dividing the corpora by length for other study.
    - The `nwl` corpus uniquely pre-arranges its contents by length, then sorts it lexicographically. So, the lexicographically-last two-letter word appears before the lexicographically-first three-letter word, etc.
9. *Are there any errors, sources of noise, or redundancies in the dataset? If so, please provide a description.*
	- Not to my knowledge.
10. *Is the dataset self-contained, or does it link to or otherwise rely on external resources (for example, websites, tweets, other datasets)? If it links to or relies on external resources, a) are there guarantees that they will exist, and remain constant, over time; b) are there official archival versions of the complete dataset (that is, including the external resources as they existed at the time the dataset was created); c) are there any restrictions (for example, licenses, fees) associated with any of the external resources that might apply to a dataset consumer? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points, as appropriate.*
	- The datasets are self-contained as text files; as long as at least one instance of these files exists, the wordlists as curated sets persist.
    - The `linux` wordlist, in particular, is only one instance of any number of wordlists that a GNU+Linux or Debian distribution may use.
    - The other two corpora are ostensibly private intellectual works and require licensing for use in commercial projects, but both can be acquired for free online through usual search routes. I do not include specific entrypoints here to minimize legal complications from doing so, but the likelihood of legal action when the data are used for private study is low.
11. *Does the dataset contain data that might be considered confidential (for example, data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals' non-public communications)? If so, please provide a description.*
	- No.
12. *Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety? If so, please describe why.*
	- As mentioned, the datasets contain any subset of English words that might be deemed offensive or pejorative. The ideotypical "poo list" of North American cuss words is found across all corpora, but inclusions of more rare or valent terms vary.
13. *Does the dataset identify any sub-populations (for example, by age, gender)? If so, please describe how these subpopulations are identified and provide a description of their respective distributions within the dataset.*
	- N/A
14. *Is it possible to identify individuals (that is, one or more natural persons), either directly or indirectly (that is, in combination with other data) from the dataset? If so, please describe how.*
	- No.
15. *Does the dataset contain data that might be considered sensitive in any way (for example, data that reveals race or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history)? If so, please provide a description.*
	- No.

**Collection process**

1. *How was the data associated with each instance acquired? Was the data directly observable (for example, raw text, movie ratings), reported by subjects (for example, survey responses), or indirectly inferred/derived from other data (for example, part-of-speech tags, model-based guesses for age or language)? If the data was reported by subjects or indirectly inferred/derived from other data, was the data validated/verified? If so, please describe how.*
	 - Word lists were curated manually, likely based on extant English corpora (dictionaries, etc.) and recommendations for additions.
2. *What mechanisms or procedures were used to collect the data (for example, hardware apparatuses or sensors, manual human curation, software programs, software APIs)? How were these mechanisms or procedures validated?*
	- Downloaded via web browser.
3. *If the dataset is a sample from a larger set, what was the sampling strategy (for example, deterministic, probabilistic with specific sampling probabilities)?*
	- Stochastic; arguably by usage (i.e., more common words are more likely to be included).
4. *Who was involved in the data collection process (for example, students, crowdworkers, contractors) and how were they compensated (for example, how much were crowdworkers paid)?*
	- Described above. HarperCollins is a private corporation, so the creation of the corpus was likely paid labour. NASPA provides its committee members with honoraria for their work, collected from membership fees.
5. *Over what timeframe was the data collected? Does this timeframe match the creation timeframe of the data associated with the instances (for example, recent crawl of old news articles)? If not, please describe the timeframe in which the data associated with the instances was created.*
	- Each of the three corpora are a particular edition of an ongoing body of work.

**Preprocessing/cleaning/labeling**

1. *Was any preprocessing/cleaning/labeling of the data done (for example, discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)? If so, please provide a description. If not, you may skip the remaining questions in this section.*
	- Yes; only words consisting of five or more lower-case English letters without diacritics were considered.
2. *Was the "raw" data saved in addition to the preprocessed/cleaned/labeled data (for example, to support unanticipated future uses)? If so, please provide a link or other access point to the "raw" data.*
	- `/in/corpus`
3. *Is the software that was used to preprocess/clean/label the data available? If so, please provide a link or other access point.*
	- `/scripts/find_pairs.py`

**Uses**

1. *Has the dataset been used for any tasks already? If so, please provide a description.*
	- See above.
2. *Is there a repository that links to any or all papers or systems that use the dataset? If so, please provide a link or other access point.*
	- N/A
3. *What (other) tasks could the dataset be used for?*
	- Any tasks requiring a cross-sectional list of English words, without consideration for usage frequency, etc.
4. *Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses? For example, is there anything that a dataset consumer might need to know to avoid uses that could result in unfair treatment of individuals or groups (for example, stereotyping, quality of service issues) or other risks or harms (for example, legal risks, financial harms)? If so, please provide a description. Is there anything a dataset consumer could do to mitigate these risks or harms?*
	- These corpora are only reflections of the English language. Any offensive use of these lists would only be reflective of offensive use of English.
5. *Are there tasks for which the dataset should not be used? If so, please provide a description.*
	- As any given word appears an absolute maximum of once in a given corpus, the corpora should not be used for frequency- or usage-based study of English words or their contents.

**Distribution**

See [here](https://www.scrabbleplayers.org/w/NWL2020) for information on NWL licensing.
