
class Number:
    
    def __init__(self,num):
        self.__num = num
        
    def set_number(self,num):
        self.__num = num
        
    def get_number(self):
        return self.__num
        
    
class Square(Number):
    
    def __init__(self,num):
        
        Number.__init__(self,num)
        
    def get_square(self):
        return self.get_number()**2
    
class Cube(Number):
    
    def __init__(self,num):
        
        Number.__init__(self,num)
        
    def get_cube(self):
        return self.get_number()**3
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    