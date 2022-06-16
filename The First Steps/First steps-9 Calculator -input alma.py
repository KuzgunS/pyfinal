

num1= float(input("Enter the first numbah: "))

#python inputu alırken hep string olarak alıyormuş bu yüzden floata çevirdik.
#print(num1)

op= input("Enter operator: ")

num2= float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1 / num2)
else:
    print("just enter one of four arithmetic operators madafaka")




