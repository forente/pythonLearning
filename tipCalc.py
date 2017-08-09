bill  = input("what is the bill? ")
rate  = input("What is the tip precentage? ")
tip  = float (bill) * float(rate)/100
print("Your tip is $"+ str(tip))
print("Your total is ${0:.2f}".format(float(bill)+ float(tip)))
