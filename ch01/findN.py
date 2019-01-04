import numpy as np

def findN(time, func):
    n = 10
    while func(n) <= time:
        n *= 10
    n /=10
    if n < 10000:
        n = 2
        while func(n) <= time:
            n +=1
        return n - 1
    else:
        return n

def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

funcDict = {
            # "log": lambda n: np.log2(n),
            # "sqrt": lambda n: np.sqrt(n),
            "n": lambda n: n,
            "nlog": lambda n: n*np.log2(n),
            "n**2": lambda n: n**2,
            "n**3": lambda n: n**3,
            "2**n": lambda n: 2**n,
            "factorial": lambda n: factorial(n),
           }

if __name__ == "__main__":
    print(f"x^2 is equal 16 when {findN(16, lambda x: x**2)}.")
    print(f"6! is {factorial(6)}.")
