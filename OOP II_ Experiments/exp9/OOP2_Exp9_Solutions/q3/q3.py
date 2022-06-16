
import calculator

def main():
    
    my_real=calculator.Real(3,4)
    print(my_real.add())
    print(my_real.substract())
    
    my_complex=calculator.Complex(0,8,0,2)
    my_complex.set_num1(7)
    my_complex.set_num2(1)
    print(my_complex.add())
    print(my_complex.substract())
      
main()
