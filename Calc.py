import operator

class TakeInput():
    """A class to make the first_no and second_no accessible to other functions"""
    # def __init__(self,first_number='',second_number=''):
    #     self.first_number = first_number
    #     self.second_number = second_number
        
    
    def add_numbers(self,a,b):
        """Function that adds the numbers"""
        return a + b


    def multiply_numbers(self,a,b):
        """Function that multiplies the numbers"""
        return a * b


    def divide_numbers(self,a,b):
        """Function that divides the numbers"""
        if b==0:
            return "Error: Division by zero"
        return a / b
        

    def subtract_numbers(self,a,b):
        """Function that performs the subtraction of the numbers"""
        return a - b
    