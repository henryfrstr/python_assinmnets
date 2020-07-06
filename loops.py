import random
# answer = 44

# question = 'What number am I thinking of?  '
# print("Let's play the guessing game!")

# while True:
#     guess = int(input(question))
#     if guess < answer:
#         print('Little higher')
#     elif guess > answer:
#         print('Little lower')
#     else:  # guess == answer
#         print('Are you a MINDREADER!!!')
#         break

a = [1, 2, 3, 4, 5]

b = [2, 3, 4, 5, 6]

for i, j in zip(a, b):
    print("{} * {} = {}".format(i, j, i*j))

