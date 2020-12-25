import random


def get_word():
    words = 'python', 'java', 'kotlin', 'javascript'
    word = words[random.randrange(len(words))]
    return word


def validate_letter(hint, word, letter):
    hint = list(hint)
    flag = 0
    for i in range(len(word)):
        if letter == word[i]:
            flag = flag + 1
            hint[i] = letter
    if flag == 0:
        print("That letter doesn't appear in the word")
    hint_str = ''
    for letter in hint:
        hint_str += letter
    return hint_str


def main():
    random_word = get_word()
    hint = '-' * len(random_word)
    print('H A N G M A N')
    for i in range(8):
        print('\n' + hint)
        user_letter = input('Input a letter: ')
        hint = validate_letter(hint, random_word, user_letter)
    print('\nThanks for playing!')
    print("We'll see how well you did in the next stage")


main()
