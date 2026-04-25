class Spellathon
    def __init__(self, data):
        self.data = data[1:]
        self.score = 0
        self.attempt = 0
        self.letters = data[0]
        self.remaining_words = sorted(self.data)
    
    def play(self, word):
        self.attempt += 1
        if len(word) >= 4 and word in self.data:
            self.score += 1
            self.data.remove(word)
            return ('Correct guess!')
        else:
            return('Incorrect guess!')
