import gensim.downloader

class Embedder:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Embedder()"

    def __str__(self):
        return "member of Test"

    def clean_word(self, word_to_clean):
        return ''.join(char for char in word_to_clean if char.isalpha()).lower() 

class GensimEmbedder(Embedder):

    available_models = list(gensim.downloader.info()['models'].keys())
    DEFAULT_PRETRAINED = 'glove-wiki-gigaword-50'

    def __init__(self, name, pretrained=DEFAULT_PRETRAINED):
        self.name = name
        self.model = gensim.downloader.load(pretrained)
        self.positives = []
        self.negatives = []

    def is_valid(self, word_to_embed:str):
        is_not_empty = len(word_to_embed)>=1
        try:
            is_known = self.model[word_to_embed]
            is_known = True
        except KeyError:
            is_known = False
        return is_not_empty and is_known

    def add(self, positive:str):
        clean_positive = self.clean_word(positive)
        if self.is_valid(clean_positive):
            self.positives.append(clean_positive)

    def sub(self, negative:str):
        clean_negative = self.clean_word(negative)
        if self.is_valid(clean_negative):
            self.negatives.append(clean_negative)

    def flush(self):
        self.positives = []
        self.negatives = []

    def res(self):
        print("Positives :", self.positives)
        print("Negatives :", self.negatives)
        positives = self.positives if len(self.positives)>0 else None
        negatives = self.negatives if len(self.negatives)>0 else None
        results = self.model.most_similar_cosmul(positive=positives, negative=negatives, topn=10)
        most_similar_key, similarity = results[0]
        return results
