## Common NLP tasks uning NLTK

These are a few functions for basic natural language processing tasks using Python's nltk library.

The functions do the following:

* tokenization and normalization of raw text
* removal of English stopwords
* tagging words with their part of speech
* lemmatizing rods to their most basic form (e.g. "are", "is", "am" are merged into "be")
* finding the most common words in a text

These scrips require the nltk lirary and the addition of corpus elements, like stopwords and wordnet.

To install nltk:

`$ pip install nltk`

Once inside Python:

    import nltk
    nltk.download()
    
And select "popular corpora" to get everything at once.