def printGrade(score):
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")

def main():
    score = eval(input("Enter a score: "))
    print('The  Grade is ', end='')
    printGrade(score)

main()