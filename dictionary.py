class Dictionary:

    def __init__(self):
        self.words = set()

    def check(self, word):
        return word.lower() in self.words

    def load(self, dictionary):
        with open(dictionary, "r") as file:
            for line in file:
                self.words.add(line.rstrip("\n"))
        return True

    def size(self):
        return len(self.words)

    def unload(self):
        return True