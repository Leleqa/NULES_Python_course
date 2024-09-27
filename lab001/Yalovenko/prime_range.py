def is_prime(num):
    if num > 1:
        for i in range(2, (num//2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def prime_range(num1, num2):
    primeList = []
    for i in range(num1, num2):
        if is_prime(i) is True:
            primeList.append(i)
    return primeList


primeList = []
print("Enter numbers to define a prime search range: ")
num1 = int(input("Number a: "))
num2 = int(input("Number b: "))


primeList = prime_range(num1, num2)

for i in primeList:
    print(str(i) + " ", end="")
print("")
