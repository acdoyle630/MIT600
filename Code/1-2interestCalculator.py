##Now write a program that calculates the minimum fixed monthly payment needed in order pay
##off a credit card balance within 12 months. We will not be dealing with a minimum monthly
##payment rate.

##Take as raw_input() the following floating point numbers:

##1. the outstanding balance on the credit card
##2. annual interest rate as a decimal

##Print out the fixed minimum monthly payment, number of months (at most 12 and possibly less
##than 12) it takes to pay off the debt, and the balance (likely to be a negative number).

##Assume that the interest is compounded monthly according to the balance at the start of the
##month (before the payment for that month is made). The monthly payment must be a multiple of
##$10 and is the same for all months. Notice that it is possible for the balance to become negative
##using this payment scheme. In short:

##Monthly interest rate = Annual interest rate / 12.0
##monthly payment

oustandingBalance = raw_input("Oustanding balance: ")
annualInterestRate = raw_input("Annual Interest Rate: ")

minimumMonthlyPayment = 0.00
totalPaid = 0.00
month = 1
originalBalance = float(oustandingBalance)


while totalPaid < originalBalance:
  minimumMonthlyPayment = minimumMonthlyPayment + 10.00
  oustandingBalance = originalBalance
  totalPaid = 0.00
  for i in range(1,13):
    interestPaid = round(float(annualInterestRate)/12 * float(oustandingBalance), 2)
    principlePaid = round(float(minimumMonthlyPayment) - float(interestPaid), 2)
    totalPaid = totalPaid + principlePaid
    oustandingBalance = float(oustandingBalance) - float(principlePaid)
    month = i
    if totalPaid >= originalBalance:
      break


print "MONTH: " + str(month)
print "MINMUM: " + str(minimumMonthlyPayment)
print "TOTAL PAID: " + str(totalPaid)

