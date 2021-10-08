class Loan:
    def __init__(self, annualInterestRate = 2.5, numberOfYears = 1, loanAmount = 1000, borrower = " "):
        self.__annualInterestRate = annualInterestRate
        self.__numberOfYears = numberOfYears
        self.__loanAMount = loanAmount
        self.__borrower = borrower

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def getNumberOfYears(self):
        return self.__numberOfYears

    def getLoanAmount(self):
        return self.__loanAMount

    def getBorrower(self):
        return self.__borrower

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def setNumberOfYears(self, numberOfYears):
        self.__numberOfYears = numberOfYears

    def setLoanAmount(self, loanAmount):
        self.__loanAMount = loanAmount

    def setBorrower(self, borrower):
        self.__borrower = borrower

    def getMonthlyPayment(self):
        monthlyInterestRate = self.__annualInterestRate / 1200
        monthlyPayment = self.__loanAMount * monthlyInterestRate / (1 - (1 / (1 + monthlyInterestRate) ** (self.__numberOfYears * 12)))
        return monthlyPayment

    def getTotalPayment(self):
        totalPayment = self.getMonthlyPayment() * self.__numberOfYears * 12
        return totalPayment
        

def main():
    # Enter each yearly interest rate
    annualInterestRate = eval(input("Enter yearly interest rate, for example, 7.25: " ))

    # Enter number of years
    numberOfYears = eval(input("Enter number of years as an integer: "))

    # Enter loan amount
    loanAmount = eval(input("Enter loan amount, for example, 120000.65: "))

    # Enter a borrower 
    borrower = input("Enter a borrower's name: ")

    # create a loan object
    loan = Loan(annualInterestRate, numberOfYears, loanAmount, borrower)

    # Display borrower's name, monthly payment, and total payment
    print("The loan is for", loan.getBorrower())
    print("The monthly payment is", format(loan.getMonthlyPayment(), ".2f"))
    print("The total payment is", format(loan.getTotalPayment(), ".2f"))

main()