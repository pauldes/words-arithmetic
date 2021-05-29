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

    def add(self, positives, negatives):
        result = self.model.most_similar_cosmul(positive=['woman', 'king'], negative=['man'], topn=3)
        most_similar_key, similarity = result[0]
        print(f"{most_similar_key}: {similarity:.4f}")
