import tkinter
from tkinter import *

class A:
    def __init__(self):
        self.objtk = Tk()
        self.objtk.title("Calculator")
        self.objtk.config(bg="lightyellow")
        self.objtk.geometry("{}x{}+0+0".format(self.objtk.winfo_screenwidth(), self.objtk.winfo_screenheight()))

        # Create a frame with a border around the calculator
        self.frame = Frame(self.objtk, bg="skyblue", bd=5)  
        self.frame.place(x=400, y=100, width=750, height=600) 

        # Creating Entry fields for numbers and operations
        self.en1 = Entry(master=self.frame, font=('consolas', 25, "bold"), bd=15, relief="sunken")
        self.en1.place(x=2, y=10, width=200, height=120)

        self.en2 = Entry(master=self.frame, font=('consolas', 25, "bold",), bd=15, relief="sunken")
        self.en2.place(x=280, y=10, width=220, height=120)

        self.result = Entry(master=self.frame, font=('consolas', 25, "bold"), bd=15, relief="sunken")
        self.result.place(x=500, y=10, width=260, height=120)

        self.operator = Entry(master=self.frame, font=('consolas', 35, "bold"), bd=18, relief="sunken")
        self.operator.place(x=202, y=10, width=77, height=120)

        self.en1.config(bg="lightgreen")
        self.en2.config(bg="lightgreen")
        self.result.config(bg="lightgreen")
        self.operator.config(bg="lightgreen")

        # Buttons for digits 0-9
        self.create_digit_buttons()

        # Arithmetic operation buttons (Updated)
        self.btn_add = Button(master=self.frame, text="+", font=('consolas', 16, "bold"), command=lambda: self.set_operator("+"), bd=10, relief="raised")
        self.btn_add.place(x=60, y=180, width=100, height=50)

        self.btn_sub = Button(master=self.frame, text="-", font=('consolas', 16, "bold"), command=lambda: self.set_operator("-"), bd=10, relief="raised")
        self.btn_sub.place(x=200, y=180, width=100, height=50)

        self.btn_mul = Button(master=self.frame, text="x", font=('consolas', 16, "bold"), command=lambda: self.set_operator("x"), bd=10, relief="raised")
        self.btn_mul.place(x=350, y=180, width=100, height=50)

        self.btn_div = Button(master=self.frame, text="/", font=('consolas', 16, "bold"), command=lambda: self.set_operator("/"), bd=10, relief="raised")
        self.btn_div.place(x=500, y=180, width=100, height=50)

        # Additional buttons
        self.btn_clear = Button(master=self.frame, text="c\nl\ne\na\nr", font=('consolas', 20, "bold"), command=self.clear, bd=10, relief="raised")
        self.btn_clear.place(x=650, y=180, width=50, height=180)

        self.btn_close = Button(master=self.frame, text="Close", font=('consolas', 16, "bold"), command=self.objtk.quit, bd=10, relief="raised")
        self.btn_close.place(x=500, y=430, width=100, height=50)

        self.btn_equal = Button(master=self.frame, text="=", font=('consolas', 16, "bold"), command=self.equal, bd=10, relief="raised")
        self.btn_equal.place(x=500, y=270, width=100, height=50)

        self.btn_backspace = Button(master=self.frame, text="X", font=('consolas', 16, "bold"), command=self.backspace, bd=10, relief="raised")
        self.btn_backspace.place(x=650, y=430, width=50, height=50)

        self.btn_switch = Button(master=self.frame, text="->/<-", font=('consolas', 16, "bold"), command=self.switch_field, bd=10, relief="raised")
        self.btn_switch.place(x=500, y=350, width=100, height=50)

        # Initialize variables
        self.current_field = self.en1
        self.operator_value = ""  # Store operator separately

        self.objtk.mainloop()

    def create_digit_buttons(self):
        # Create buttons for digits 0-9
        digit_buttons = [
            (0, 200, 530), (1, 60, 270), (2, 200, 270), (3, 340, 270),
            (4, 60, 350), (5, 200, 350), (6, 340, 350), (7, 60, 430),
            (8, 200, 430), (9, 340, 430)
        ]
        
        for digit, x, y in digit_buttons:
            Button(self.frame, text=str(digit), font=('consolas', 16, "bold"), 
                   command=lambda d=digit: self.append_digit(d), bd=10, relief="raised").place(x=x, y=y, width=100, height=50)

    def append_digit(self, digit):
        current_value = self.current_field.get()
        self.current_field.delete(0, END)
        self.current_field.insert(0, current_value + str(digit))

    def clear(self):
        self.en1.delete(0, END)
        self.en2.delete(0, END)
        self.operator.delete(0, END)
        self.result.delete(0, END)

    def set_operator(self, operator_symbol):
        """Set the selected operator and display it in the operator Entry field"""
        self.operator_value = operator_symbol
        self.operator.delete(0, END)
        self.operator.insert(0, operator_symbol)  # Display operator
        self.num1 = float(self.en1.get())  # Store the first number
        self.current_field = self.en2
        self.en2.focus()

    def equal(self):
        try:
            num2 = float(self.en2.get())  # Get the second number
            if self.operator_value == "+":
                result = self.num1 + num2
            elif self.operator_value == "-":
                result = self.num1 - num2
            elif self.operator_value == "x":
                result = self.num1 * num2
            elif self.operator_value == "/":
                if num2 == 0:
                    self.result.delete(0, END)
                    self.result.insert(0, "Cannot divide by 0")
                    return
                result = self.num1 / num2

            self.result.delete(0, END)
            self.result.insert(0, str(result))

        except ValueError:
            self.result.delete(0, END)
            self.result.insert(0, "Error")

    def backspace(self):
        current_value = self.current_field.get()
        if len(current_value) > 0:
            self.current_field.delete(len(current_value) - 1, END)

    def switch_field(self):
        if self.current_field == self.en1:
            self.current_field = self.en2
            self.en2.focus()
        elif self.current_field == self.en2:
            self.current_field = self.en1
            self.en1.focus()

# Running the calculator
win = A()
