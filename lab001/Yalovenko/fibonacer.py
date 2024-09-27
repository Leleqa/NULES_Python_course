def fib(k):
    if k == 1:
        return [0]
    elif k == 2:
        return [0, 1]
    else:
        fib_list = fib(k - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list


k = int(input("Enter a number of fibonacci numbers you would like to get: "))
fib_sequence = fib(k)
print(f"First {k} Fibonacci numbers: {fib_sequence}")
