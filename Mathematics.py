while True:
        choice = int(input('[0] Exit [1] Addition [2] Subtraction [3] Multiplication [4] Division : '))
        x = 0.0
        num1 = 0
        num2 = 0
        if ((choice > 0) and (choice < 5)):
                num1 = float(input('Enter the first number: '))
                num2 = float(input('Enter the second number: '))
                if(choice == 1):
                        x = num1 + num2
                elif(choice == 2):
                        x = num1 - num2
                elif(choice == 3):
                        x = num1 * num2
                elif(choice == 4):
                        x = num1 / num2
                print("The output is: %f" % (x))
        elif (choice == 0):
                print("Annyeong!")
                break
        else:
                print("The choice is invalid.")
                
