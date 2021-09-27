# Return the gcd of two integers

def gcd(n1, n2):
    gcd = 1
    k = 2

    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k 
        k += 1

    return gcd

n1 = eval(input("Enter the first integer: "))
n2 = eval(input("Enter the second integer: "))

print("The greatest common divisor for", n1, "and", n2, "is", gcd(n1, n2))