#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count_down = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 'Happy New Year!']
    for num in count_down:
        print(num)

def square_integers(int_list):
    # code goes here!
    squared = list()
    for num in int_list:
        squared.append(num ** 2)
    return squared

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)