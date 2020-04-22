while True:
    number = input("Enter a positive Number:")
    numberofdigits = len(number)
    summ = 0

    if number.isnumeric():

        for i in range(numberofdigits):
            summ += int(number[i]) ** numberofdigits

        if summ == int(number):
            print(number, "is a Amstrong Number.")
        else:
            print(number, "is not a Amstrong Number.")

    elif number.count(".") == 1 or number.count(",") == 1:
        print("Please enter a integer number.")

    else:
        if number.count("-") == 1 and number.index("-") == 0 and number.replace("-", "1").isnumeric():
            print("Please enter a positive number")
        else:
            print("Do not use any entries other than numeric values")
