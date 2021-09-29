# convert a decimal to a hex as a string

def decimalTohex(decimalValue):
    hex = ""

    while decimalValue != 0:
        hexValue = decimalValue % 16
        hex = toHexChar(hexValue) + hex
        decimalValue = decimalValue // 16

    return hex

# convert an integer to a single hex digit as a character
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('O'))
    else: # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord('A'))

def main():
    # prompt the user to enter a positive integer
    decimalValue = eval(input("Enter a decimal number: "))

    print("The hex number for decimal", decimalValue, "is", decimalTohex(decimalValue))

main()