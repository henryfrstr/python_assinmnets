number = int(input("Enter a number: "))

primes = []
for prime in range(2, number + 1):
    is_prime = True
    for num in range(2, prime):
        if prime % num == 0:
            is_prime = False
    if is_prime:
        primes.append(prime)
print(primes)
