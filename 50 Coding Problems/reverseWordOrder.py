print('Please type a sentence and the order of the words will be reversed.')
user_input = input()

list1 = user_input.split()
sentence = ' '.join((list1[::-1]))
print(sentence)