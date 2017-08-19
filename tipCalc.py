bill  = 0;
rate  = 0;
tip = 0;

def getInput (text):
    num = True
    i = 0
    while num:
        try:
            i = float(input(text))
            num = False
        except ValueError:
            num = True
            print("Please enter a number. ")
    return i

bill  = getInput("what is the bill? ")
rate  = getInput("What is the tip precentage? ")
tip  = (bill * rate) /100
print("Your tip is $"+ str(tip))
print("Your total is ${0:.2f}".format(float(bill)+ float(tip)))
