word = input('This is a vowel counter. Please input a word.    ')

vowels = ['a', 'e', 'i', 'o', 'u']


def vowelCounter(word):
    wordList = list(word)
    print(wordList)
    counter = 0
    
    for i in wordList:
        if i in vowels:
            counter = counter + 1

    print(counter)

vowelCounter(word)