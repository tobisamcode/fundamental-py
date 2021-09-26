# Return grade for the score 
def getGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    

def main():
    score = eval(input("Enter a score: "))
    print("The grade is ", getGrade(score))

main()

'''The getGrade function defined in lines 2–12 returns a character grade based on the
numeric score value. It is invoked in line 16.
The getGrade function returns a character, and it can be invoked and used just like a
character. The printGrade function does not return a value, and it must be invoked as a
statement.''' 