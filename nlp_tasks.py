import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

engstopwords = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(treebank_tag):
    """Utility function to convert pos_tag part-of-speech tags 
    to WordNet tags for use with lemmatizer. 
    """
    
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None # for easy if-statement 

def tokenize(text):
    """Takes raw text, tokenizes it, removes stopwords 
    and words that are one-character long (like 'a' and punctuation).
    Returns a list of tokens.
    """
    
    tokens = nltk.tokenize.word_tokenize(text)
    tokens = [word.lower() for word in tokens if len(word) > 1]
    tokens = [word for word in tokens if word not in engstopwords]
    return tokens

def get_pos(tokens):
    """Takes a token list and gets the part-of-speech for each.
    Returns a list of tuples ('word', 'POS')
    """
    
    tagged = nltk.pos_tag(tokens)
    return tagged
  
def lemmatize(tagged_words):
    """Lemmatizes words. That is, it normalizes words to their most
    basic form. For example, 'is', 'am' and 'are' are merged into 'be'.
    
    Returns a list of lemmatized tokens.
    
    Lemmatization is confined to parts of speech. Verb variations are lemmatized
    to the root verb, and same with nouns.
    
    Example: 'continues' and 'continuing' are merged to 'continue'
    but 'continuation' stays the same.
    """
    
    lemma_list = []
    for word, tag in tagged_words:
        wntag = get_wordnet_pos(tag)
        if wntag is None:
            lemma = lemmatizer.lemmatize(word) 
        else:
            lemma = lemmatizer.lemmatize(word, pos=wntag)
        lemma_list.append(lemma)
    return lemma_list
  
def get_distfreq(tokens, top_n):
    """ Finds the most common words in a token list.
    Returns a list of tuples ('word', frequency)
    """
    
    fdist = nltk.FreqDist(tokens)
    return fdist.most_common(top_n)

def sentiment_analysis(text)
    """Prints out the VADER sentiment scores for each sentence in the text."""
    
    sentences = sent_tokenize(text)
    pos = []
    neg = []
    neu = []
    for sentence in sentences:
        ss = sia.polarity_scores(sentence)
        if ss['neu'] > 0.5:
            neu.append(sentence)
        elif: ss['pos'] > 0.5:
            pos.append(sentence)
        else:
            neg.append(sentence)
        
    print("Positive: {}, Negative: {}, Neutral: {} ".format(str(len(pos)), str(len(neg)), str(len(neu))))
        #for k in ss:
        #    print('{0}: {1}, '.format(k, ss[k]))
        #    print('\n')