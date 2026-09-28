while True:
    inputValue = input("Enter a valid number:")
    if inputValue.isdigit():
        intValue = int(inputValue)
        revNumber = ""
        
        while (intValue>0):
            digit = intValue%10
            intValue = intValue//10
            revNumber = revNumber+""+str(digit)
        
        print("Reverse Number :",revNumber)
    else:
        print("Your entered wrong number. Please retry. ")
        y = input("Do you want to continue..(y/n)")
        if y.lower()=='n':
          break