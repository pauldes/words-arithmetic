class Embedder:
    def __init__(self, name):
        self.name = name
    
    def printname(self):
        print(self.name)

    def __repr__(self):
        return "Embedder()"

    def __str__(self):
        return "member of Test"