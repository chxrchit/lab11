class Spellathon:
    def __init__(self, data):
        self.letters = data[0]
        self.data = data[1:]
        self.score = 0
        self.attempts = 0
        self.remaining_words = sorted(self.data)

    def play(self, word):
        self.attempts += 1
        if len(word) >= 4 and word in self.data:
            self.score += 1
            self.data.remove(word)
            self.remaining_words = sorted(self.data)
            return 'Correct guess!'
        return 'Incorrect guess!'
