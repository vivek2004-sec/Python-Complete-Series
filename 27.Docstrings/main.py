def square(n):
    
    '''Takes in a number n, returns the square of n.'''
    print(n**2)

square(5)
print(square.__doc__)


def average(a, b):
    '''Takes the sum of the a +b and divide by 2'''

    average = a +b / 2
    print(average)

a = 5
b = 6
average(a,b)
print(average.__doc__)
