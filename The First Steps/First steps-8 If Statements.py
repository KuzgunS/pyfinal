is_male = True
is_tall = True


if is_male:
    print("you got a diiieck")
else:
    print("M'lady")

if is_male and is_tall:
    print("I guess you got a \"tall dick\" ")

if is_male or is_tall:
    print("You are male or tall")

print("elif part:\n")

if not(is_male and is_tall):
    print("wont be printed")
elif(not(is_male)):
    print("wont be printed")
else:
    print("you are printed sir.")



print("If comparisons\n")

number1= 1
number2= 3
number3= 6

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print("num 1 is the biggest")
        return num1
    elif num2 >= num1 and num2 >= num3:
        print("num 2 is the biggest")
        return num2
    else:
        print("num 3 is the biggest")
        return num3

max_num(number1,number2,number3)

def compare_string(str1, str2, str3):
    if str1 == str2:
        print(str3)
    else:
       print("strings aren't same")

compare_string("anan","anan","strler eşit hacım")


