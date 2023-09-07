#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        if i == 1:
            print("Happy New Year!")
        i -= 1
        


def square_integers(int_list):
    # for num in int_list:
    #     print(num)
    return [num ** 2 for num in int_list]

def fizzbuzz():
    for i in range(100):
        i+=1
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()