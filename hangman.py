import random


def get_word():
    words = 'python', 'java', 'kotlin', 'javascript'
    word = words[random.randrange(len(words))]
    return word


def get_hint(word):
    hint = word[:3]
    for i in range(3, len(word)):
        hint = hint + '-'
    return hint


def validate_word(word, user_word):
    if user_word == word:
        print('You survived!')
        return 1
    else:
        print('You lost!')
        return 0


def main():
    random_word = get_word()
    hint = get_hint(random_word)
    print('H A N G M A N')
    user_word = input('Guess the word ' + hint + ': ')
    validate_word(random_word, user_word)


main()
