num = int(input("Enter a number: "))
a = 1
b = 1
fibonacci = [a, b]

while a + b <= num:
    a, b = b, a + b
    fibonacci.append(b)
print(fibonacci)
