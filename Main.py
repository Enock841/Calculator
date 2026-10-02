"""A SIMPLE CALCULATOR THAT PERFORMS BASIC OPERATIONS"""
import tkinter as tk
from Calc import TakeInput


class CalcApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")
        

        self.Calc = TakeInput()

        #Input fields
        tk.Label(root, text = "First Number:").grid(row=0, column=0,padx=5,pady=5)
        self.first_entry = tk.Entry(root)
        self.first_entry.grid(row=0,column=1,padx=80,pady=60)

        tk.Label(root, text="Second Number:").grid(row=1,column=0)
        self.second_entry = tk.Entry(root)
        self.second_entry.grid(row=1,column=1,padx=5,pady=5)

        #Result display
        self.result_label = tk.Label(root, text="Result: ")
        self.result_label.grid(row=2,column=0,columnspan=2)

        # Buttons for operation
        tk.Button(root, text="Add", command=self.add_numbers).grid(row=3,column=0, sticky="ew",padx=5,pady=5)
        tk.Button(root, text="Subtract",command=self.subtract_numbers).grid(row=4,column=0,sticky="ew",padx=5,pady=5)
        tk.Button(root,text="Multiply",command=self.multiply_numbers).grid(row=5,column=0,sticky="ew",padx=5,pady=5)
        tk.Button(root,text="Divide",command=self.divide_numbers).grid(row=6,column=0,sticky="ew",padx=5,pady=5)


    def take_inputs(self):
        """Accepts the numbers to be operated on"""
        try:
            a = float(self.first_entry.get())
            b = float(self.second_entry.get())
            return a, b
                
        except (TypeError,ValueError):
            self.result_label.config(text="Invalid Input!!")
            return None, None
        

    def add_numbers(self):
        a,b = self.take_inputs()
        if a is not None:
            result = self.Calc.add_numbers(a,b)
            self.result_label.config(text=f"Result: {result}")


    def subtract_numbers(self):
        a,b = self.take_inputs()
        if a is not None:
            result = self.Calc.subtract_numbers(a,b)
            self.result_label.config(text=f"Result: {result}")  


    def multiply_numbers(self):
        a,b = self.take_inputs()
        if a is not None:
            result = self.Calc.multiply_numbers(a,b)
            self.result_label.config(text=f"Result: {result}")     
        
    def divide_numbers(self):
        a,b = self.take_inputs()
        if a is not None:
            result = self.Calc.divide_numbers(a,b)
            self.result_label.config(text=f"Result: {result}")


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(300,200)
    root.maxsize(600,400)
    app = CalcApp(root)
    root.mainloop()

