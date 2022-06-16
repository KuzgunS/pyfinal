
class Real:
    
    def __init__(self,n1,n2):
        self.__num1 = n1
        self.__num2 = n2
        
    def set_num1(self,n1):
        self.__num1 = n1
        
    def set_num2(self,n2):
        self.__num2 = n2
        
    def get_num1(self):
        return self.__num1
        
    def get_num2(self):
        return self.__num2
        
    def add(self):
        return self.__num1+self.__num2
    
    def substract(self):
        return self.__num1-self.__num2
   
    
class Complex(Real):
    
    def __init__(self,r1,i1,r2,i2):
        
        Real.__init__(self,r1,r2)
        
        self.__imag1 = i1
        self.__imag2 = i2
    
    
    def set_imag1(self,i1):
        self.__imag1 = i1
        
    def set_imag2(self,i2):
        self.__imag1 = i2
        
    def get_imag1(self):
        return self.__imag1
        
    def get_imag2(self):
        return self.__imag2
        
    def add(self):
        return self.get_num1()+self.get_num2(), self.__imag1+self.__imag2
    
    def substract(self):
        return self._Real__num1-self._Real__num2,self.__imag1-self.__imag2
   

    
    

    
    
    
    
    