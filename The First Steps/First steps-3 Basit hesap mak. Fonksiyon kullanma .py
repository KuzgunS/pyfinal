
print("making a simple calculator ------------------\n")

num1 = input("Enter a number: ")
num2 = input("Enter anotha number: ")
result = num1 + num2
print(result)
print("what de fuk")  #input alırken hep str alıyormuş python. O yüzden önce onları sayıya çevirmek gerekiyor.

right_result= int(num1) + int(num2) #int yazınca girişte int girmen lazım. floatsa float gibi gibi. Yoksa program gg
#  print("Your right result is: " + right_result) str ve int yazıldı. str olmasını sağlamamız lazım,
print("Your right result is: " + str(right_result))



