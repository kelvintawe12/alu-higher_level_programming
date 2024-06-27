#!/usr/bin/env python3

def fizzbuzz(n):
    result = ""
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result += "FizzBuzz "
        elif i % 3 == 0:
            result += "Fizz "
        elif i % 5 == 0:
            result += "Buzz "
        else:
            result += str(i) + " "
    print(result.strip())

if __name__ == "__main__":
    fizzbuzz(100)
