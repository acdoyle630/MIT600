
oustandingBalance = raw_input("Oustanding balance: ")
annualInterestRate = raw_input("Annual Interest Rate: ")

minimumMonthlyPayment = float(oustandingBalance)/12.00
highestMonthlyPayment = float(oustandingBalance)
totalPaid = 0.00
month = 1
originalBalance = float(oustandingBalance)
guesses = 0



while totalPaid < originalBalance:
  minimumMonthlyPayment = minimumMonthlyPayment + 0.01
  guesses += 1
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

