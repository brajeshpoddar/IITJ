
while True:
    inputValue = input("Enter a number: ")
    if inputValue.isdigit():
        intVal = int(inputValue)
        sum_of_digits = 0
        while intVal >0:
            digit = intVal % 10
            intVal = intVal // 10
            sum_of_digits += digit
        print("The sum of digits is:", sum_of_digits)
    else:
        print("Your Input is not a string. Please enter a valid number.")
        y = input("Do you want to continue? (y/n): ")
        if y.lower() == 'n':
            break