class Embedder:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

    def __repr__(self):
        return "Embedder()"

    def __str__(self):
        return "member of Test"