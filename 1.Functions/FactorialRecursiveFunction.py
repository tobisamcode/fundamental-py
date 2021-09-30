'''This is a recursive function to find the factorial of an integer'''
def factorial(x):

    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))

def main():
    number = 6
    print("THe factorial of ", number, 'is', factorial(number))

main()