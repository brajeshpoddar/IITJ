

while True:
    intValue = input("Please Enter valid number:")
   
    if intValue.isdigit():
        intValue = int(intValue)
        orgVal = intValue;
        reverseValue =""
        while(intValue>0):
            digit = intValue%10;
            reverseValue = reverseValue+""+str(digit)
            intValue = intValue//10;
            
        print("Revese Value:",reverseValue)  
        if(int(orgVal) == int(reverseValue)):
            print("Given Number is Pelindrom")
            
        else:
            print("Number is not Pelindrom")
            
    else:
        print("Your input contains alphabets as well. Please i=einter valid Number")
        y = input("Do you contunue?(y/n)")
        if y.lower() =='n':
          break