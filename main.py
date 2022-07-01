#!/usr/bin/python3
import sys


def add(a, b):
    return (a + b)

def sub(a, b):
    return (a - b)

def mul(a, b):
    return (a * b)

def div(a, b):
    return (a / b)

first_val = int(sys.argv[1])
second = int(sys.argv[3])
def calculate():
    if sys.argv[2] == "+":
        return add(first_val, second)
    elif sys.argv[2] == "-":
        return sub(first_val, second)
    elif sys.argv[2] == "*":
       return mul(first_val, second)
    elif sys.argv[2] == "/":
      return div(first_val, second)
    else:
        print("invalid operator")
        exit()
if __name__ == "__main__":
    result = calculate()
    print(result)
