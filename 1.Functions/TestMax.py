# Return the max of two numbers
def max(num1, num2):
    if num1 < num2:
        result = num2
    else:
        result = num1

    return result

def main():
    m = 3
    n = 6
    k = max(m, n)
    print("The larger number of", m, "and", n, "is", k )

main()
