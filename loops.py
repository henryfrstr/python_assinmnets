
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


# a = [1, 2, 3, 4, 5]  # (1, 6)

# b = [6, 7, 8, 9, 10, 11, 12]

# c = [11, 12, 13]

# for i, j, k in zip(a, b, c):
#     print(i, j, k)
# a = dict(zip("abc", "cde"))
# print(a)


a = list(range(1, 11))
b = list(range(1, 11))

for i in a:  # 12345678910
    for j in b:
        print("{} * {} = {}".format(i, j, i*j))
