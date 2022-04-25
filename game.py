from w2vec_model import get_random_word, similarity_calc

class Game:
    def __init__(self, session_id):
        self.session_id = session_id
        self.target_word = get_random_word()
        self.guesses = []
        self.num_guesses = 0

    def make_guess(self, guess):
        self.guesses.append(guess)
        self.num_guesses += 1
        return similarity_calc(guess, self.target_word)

    
