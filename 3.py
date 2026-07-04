#  calculator using condition
# op = input("enter the operator:")
# num1 = float(input("Enter the first number:"))
# num2 = float(input("Enter the second number:"))

# if op == "+":
#     print(num1+num2)
# elif op == "-":
#     print(num1-num2)
# elif op == "*":
#     print(num1*num2)
# elif op =="%":
#     print(num1%num2)
# else:
#     print(num1/num2)

"building calculator using Function"

def calculator():
    while True:
        op = input("enter  operator(+,-,*,/,%, or exit):")
        if op == "exit":
            print("Calculator closed")
            break
        try:
            num1 = float(input("Enter the first number:"))
            num2 = float(input("Enter the second number:"))

    
            if op == "+":
                print(num1+num2)
            elif op == "-":
                print(num1-num2)
            elif op == "*":
                print(num1*num2)
            elif op =="%":
                print(num1%num2)
            elif op == "/":
                 print(num1/num2)

            else:
                print("Invalid operator!:")
        
        except :
            print("Please enter valid number,")
   
print(calculator())


    
    