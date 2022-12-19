import numpy as np
class Utils:

    @staticmethod
    def tokenize(corpus, shape):
        if shape == 'sentences':
            tk_corpus = [doc.split() for doc in corpus]
        elif shape == "bulk":
            sentences = corpus.split('.')
            tk_corpus = [doc.split() for doc in sentences]
        return tk_corpus

    @staticmethod
    def clean_docs(corpus, lang='english'):
        import string
        import nltk
        from nltk.corpus import stopwords
        from collections import defaultdict

        nltk.download('stopwords')
        stopWords = stopwords.words(lang)

        word_counts = defaultdict(int)
        clean_corpus = []
        for doc in corpus:
            new_doc = []

            for w in doc:
                word = w.translate(str.maketrans('', '', string.punctuation))\
                        .translate(str.maketrans('', '', string.digits))
                if word.lower() not in stopWords and len(word) > 1:
                    new_doc.append(word.lower())
                    # add word to word count dictionary
                    word_counts[word.lower()] += 1

            clean_corpus.append(new_doc)

        return clean_corpus, word_counts

    @staticmethod
    def vocab_idx(words):
        idx = np.arange(len(words))
        word_idx = dict(zip(sorted(words), idx))
        return word_idx

    @staticmethod
    def unigram(word_counts):
        total_words = sum([np.power(freq, 3/4) for freq in word_counts.values()])
        word_prob = {word: (np.power(freq, 3/4) / total_words) for word, freq in word_counts.items()}
        return word_prob

    @staticmethod
    def negative_sample(unigram, k):
        samples = np.random.choice(list(unigram.keys()), p=list(unigram.values()), size=k)
        return samples
