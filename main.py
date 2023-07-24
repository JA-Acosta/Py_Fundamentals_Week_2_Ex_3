'''
>>> JAAR
>>> 07/24/2023
>>> Practicing Fundamentals Program 9
>>> Version 1
'''
from math import pi

'''
>>> Generates a program that will ask the user for a number, will then determine if the number is even or odd. Afterwards, will calculate the radius of a circle using the number and finally will calculate the factorial for the number inputted.
'''
def verify_int() :
    '''
    >>> Takes a user input and verifies if it is a number or not. If the input is a number, will return it. Otherwise, will ask the user for another input.

    >>> Return: (int) number
    '''
    while True :
        try :
            number = int(input())
        except ValueError :
            print('Your input was invalid!\nPlease enter a number: ', end = '')
        else :
            return number
    pass

def is_even(number : int) :
    '''
    >>> Checks if a number is even and print the result.
    >>> Param: (int) number
    '''
    if number % 2 == 0 :
        print(f'{ number } is even.')
    else :
        print(f'{ number } is odd.')

def factorial(number : int)->int:
    '''
    >>> Calculates the factorial of a number.

    >>> Param: (int) number
    >>> Returns: answer
    '''
    if number > 0 :
        return number * factorial(number - 1)
    else:
        return 1

def main() :
    print('Enter a number: ', end = '')
    number = verify_int()
    is_even(number)
    circle_area = lambda radius : pi * radius ** 2
    print(f'The area for a circle of radius { number } is { circle_area(number) }.')

    print(f'{ number }! = { factorial(number) }')
if __name__ == '__main__' :
    main()