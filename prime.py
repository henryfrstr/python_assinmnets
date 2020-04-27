while True:
    num = int(input("Enter a number: "))
    div = 0
    if num > 1:
        for i in range(2, num):
            if num % i != 0:
                div += 1
            else:
                div += 0
        if div == 0:
            print(num, "is a prime number")
        else:
            print(num, "is not a prime number")
    else:
        print(num, "is not a prime number")
