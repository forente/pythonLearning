bill  = int(input("what is the bill? "))
rate  = int(input("What is the tip precentage? "))
tip  = bill * rate/100
print("Your tip is $"+ str(tip))
print("Your total is $ {0:.2f}".format(bill+tip))
