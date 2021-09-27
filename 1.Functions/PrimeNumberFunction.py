''' PrimeNumber.py . The program defines two new functions, isPrime and
printPrimeNumbers . The isPrime function determines whether a number is prime, and
the printPrimeNumbers function prints prime numbers. '''

# Check whether number is prime
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            #if true, it is not prime
            return False
        divisor += 1

    return True


def printPrimeNumbers(numberOfPrimes):
    NUMBER_OF_PRIMES = 50 # Number of primes to display
    NUMBER_OF_PRIMES_PER_LINE = 10 # Display 10 per line
    Count = 0 # count the number of prime numbers
    number = 2 # A number to be tested for primesness

    # Repeatedly find prime numbers
    while Count < NUMBER_OF_PRIMES:
        # Print the prime numbers and increase the count
        if isPrime(number):
            Count += 1 #INcrease the counts

            print(number, end=" ")
            if Count % NUMBER_OF_PRIMES_PER_LINE == 0:
                # print the prime numbers and advanced to the new line
                print()

        # check if the next number is prime
        number += 1

def main():
    print("The first 50 prime numbers are")
    printPrimeNumbers(50)


main()