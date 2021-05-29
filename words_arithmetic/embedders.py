import gensim.downloader

class Embedder:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Embedder()"

    def __str__(self):
        return "member of Test"

class GensimEmbedder(Embedder):
    def __init__(self, name, pretrained='glove-wiki-gigaword-50'):
        self.name = name
        self.model = gensim.downloader.load(pretrained)
        self.positives = []
        self.negatives = []

    def add(self, positive:str):
        self.positives.append(positive)

    def sub(self, negative:str):
        self.negatives.append(negative)

    def res(self):
        print(self.positives)
        print(self.negatives)
        results = self.model.most_similar_cosmul(positive=self.positives, negative=self.negatives, topn=3)
        most_similar_key, similarity = results[0]
        return f"{most_similar_key}: {similarity:.4f}"
