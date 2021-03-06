import abc

import gensim.downloader

class Embedder(metaclass=abc.ABCMeta):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Embedder(name={self.name})"

    def __str__(self):
        return f"An Embedder named {self.name}."

    def clean_word(self, word_to_clean):
        return ''.join(char for char in word_to_clean if char.isalpha()).lower() 

    @classmethod
    @abc.abstractmethod
    def available_models(cls):
        pass

    @abc.abstractmethod
    def add(self, positive:str):
        pass

    @abc.abstractmethod
    def sub(self, negative:str):
        pass

    @abc.abstractmethod
    def res(self):
        pass

    @abc.abstractmethod
    def flush(self):
        pass

class GensimEmbedder(Embedder):

    def __init__(self, name, pretrained='glove-twitter-25'):
        self.name = name
        self.model = gensim.downloader.load(pretrained)
        self.positives = []
        self.negatives = []

    @classmethod
    def available_models(cls):
        return list(gensim.downloader.info()['models'].keys())

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
        results = self.model.most_similar_cosmul(positive=positives, negative=negatives, topn=5)
        return dict(results)
