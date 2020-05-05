for num in range(1, 101):
    print('Fizz' * (num % 3 == 0) + 'Buzz' * (num % 5 == 0) or num)
