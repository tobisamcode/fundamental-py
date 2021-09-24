def sum(i1, i2):
    result = 0
    for i in range (i1, i2 + 1):
        result += i

    return result

def main():
    print('sum from 1 to 10 is', sum(1, 10))
    print('sum from 1 to 10 is', sum(20, 37))
    print('sum from 1 to 10 is', sum(35, 40))

main() # call the function