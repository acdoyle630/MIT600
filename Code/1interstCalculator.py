##Write a program to calculate the credit card balance after one year if a person only pays the
##minimum monthly payment required by the credit card company each month.

##Use raw_input() to ask for the following three floating point numbers:

##1. the outstanding balance on the credit card
##2. annual interest rate
##3. minimum monthly payment rate

##For each month, print the minimum monthly payment, remaining balance, principle paid in the
##format shown in the test cases below. All numbers should be rounded to the nearest penny.

##Finally, print the result, which should include the total amount paid that year and the remaining
##balance.
##

oustandingBalance = float(raw_input("Outstanding balace: "))
annualInterestRate = float(raw_input("Annual Interest Rate: "))
minimumMonthlyPaymentRate = float(raw_input("Minimum Monthly Payment Rate: "))

month = 1
totalAmountPaid = 0
remainingBalance = oustandingBalance

for i in range(1,13):
  minimumMonthlyPayment = round(oustandingBalance * minimumMonthlyPaymentRate, 2)
  interestPaid = round(annualInterestRate/12 * oustandingBalance, 2)
  principlePaid = round(minimumMonthlyPayment - interestPaid, 2)
  remainingBalance = round(oustandingBalance - principlePaid, 2)
  print "Month: " + str(i)
  print "Minimum Monthly Payment: $" + str(minimumMonthlyPayment)
  print "Principle Paid: $" + str(principlePaid)
  print "Remaing Balance: $" + str(remainingBalance)
  oustandingBalance = remainingBalance
  totalAmountPaid = totalAmountPaid + minimumMonthlyPayment
  remainingBalance = oustandingBalance

print "Total amount paid: $" + str(totalAmountPaid)
print "Remaing Balance: $" + str(remainingBalance)

