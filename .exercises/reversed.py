word = input('Type a word: ')

reversed_word = word[::-1]

if word == reversed_word:
    print(f'{word} is the same as reversed')
else:
    print(f'{word} is not the same as reversed')
