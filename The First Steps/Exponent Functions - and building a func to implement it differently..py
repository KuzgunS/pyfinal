print(2**3) # 2^3 demek.


def raise_to_power(base,power): # for loop ile de bunu sağlayan bir fonksiyon yapmış olduk.
    result = 1
    for i in range(power):
        result *= base
    return result


print(raise_to_power(3,4))







