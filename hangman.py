import random


class HangmanGame:
    def __init__(self):
        self.game_words = 'python', 'java', 'kotlin', 'javascript'
        self.random_word = ''
        self.hint = ''
        self.lives = 7

    def get_word(self):
        self.random_word = self.game_words[random.randrange(len(self.game_words))]
        self.hint = '-' * len(self.random_word)

    def check_input(self, user_input):
        hint = list(self.hint)
        flag = 0
        for i in range(len(self.random_word)):
            if (user_input == self.hint[i]) and (user_input != '-'):
                self.count_lives(-1)
                flag = flag + 1
                print('No improvements')
                break
            if user_input == self.random_word[i]:
                flag = flag + 1
                hint[i] = user_input
        if flag == 0:
            self.count_lives(-1)
            print("That letter doesn't appear in the word")
        hint_str = ''
        for letter in hint:
            hint_str += letter
        self.hint = hint_str
        if self.hint == self.random_word:
            self.lives = -1
            print('\n' + self.hint)
            print('You guessed the word!')
            print('You survived!')

    def count_lives(self, number):
        self.lives += number
        if self.lives < 0:
            print('You lost!')


def main():
    game = HangmanGame()
    game.get_word()
    print('H A N G M A N')
    while game.lives >= 0:
        print('\n' + game.hint)
        user_letter = input('Input a letter: ')
        game.check_input(user_letter)


main()

