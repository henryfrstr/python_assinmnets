print("Presss 'q' for quit.")
while True:
    number = input("Enter a positive Number:").strip().lower()
    numberofdigits = len(number)
    summ = 0

    if number == "q":
        print("See you...")
        break

    else:
        if number.isnumeric():
            for i in range(numberofdigits):
                summ += int(number[i]) ** numberofdigits

            if summ == int(number):
                print(number, "is a Amstrong Number.")

            else:
                print(number, "is not a Amstrong Number.")

        elif number.count(".") == 1 and number.replace(".", "1").isnumeric() or number.count(",") == 1 and number.replace(",", "1").isnumeric():
            print("Please enter a integer number.")

        elif number.count("-") == 1 and number.index("-") == 0 and number.replace("-", "1").isnumeric():
            print("Please enter a positive number")

        else:
            print("Do not use any entries other than numeric values")

# number = input("Please enter a positive integer number _  ")
# results = {
#     0: f'{number} is not an Armstrong number',
#     1: f'{number} is an Armstrong number',
#     2: 'Please enter a positive number',
#     3: 'Please enter an integer number',
#     4: 'Do not use entries other than numeric values'
# }
# if number[0] == '-':
#     print(results[2])
# elif number.count(',') + number.count('.') != 0:
#     print(results[3])
# elif not number.isnumeric():
#     print(results[4])
# else:
#     is_arm = 0
#     for i in number:
#         is_arm += int(i) ** len(number)
#     print(results[is_arm == int(number)])
