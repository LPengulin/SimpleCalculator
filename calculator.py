import os
from customtkinter import CTk, CTkButton, CTkEntry, END, StringVar
from colors import allColors


class Calculator(CTk):

    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.resizable(False, False)
        self._set_appearance_mode("dark")
        self.config(background=allColors["mountbatten"])
        self.iconbitmap(os.path.join(os.getcwd(), 'assets', 'icon.ico'))
        

        #creating the entry widget
        self.entry_text = StringVar()
        self.entry = CTkEntry(self, width=270, bg_color=allColors["mountbatten"], height=40, fg_color=allColors["entryBack"], border_color=allColors["mountbatten"], text_color=allColors["lavender"], textvariable=self.entry_text)
        self.entry_text.trace("w", self.isString)

        #creating the buttons
        self.createButtons()

        self.buttonAdd = CTkButton(self, text="+", corner_radius=5, width=170, height=40, bg_color=allColors["mountbatten"], fg_color=allColors["dogwood"], text_color=allColors["black"], hover_color=allColors["darkDogwood"], command=self.add_button)
        self.buttonMinus = CTkButton(self, text="-", corner_radius=5, width=80, height=40, bg_color=allColors["mountbatten"], fg_color=allColors["dogwood"], text_color=allColors["black"], hover_color=allColors["darkDogwood"], command=self.minus_button)
        self.buttonMultiply = CTkButton(self, text="\u00D7", corner_radius=5, width=80, height=40, bg_color=allColors["mountbatten"], fg_color=allColors["dogwood"], text_color=allColors["black"], hover_color=allColors["darkDogwood"], command=self.multiply_button)
        self.buttonDivide = CTkButton(self, text='\u00F7', corner_radius=5, width=80, height=40, bg_color=allColors["mountbatten"], fg_color=allColors["dogwood"], text_color=allColors["black"], hover_color=allColors["darkDogwood"], command=self.divide_button)

        self.buttonClear = CTkButton(self, text="C", corner_radius=5, width=80, height=40, bg_color=allColors["mountbatten"], fg_color=allColors["wine"], hover_color=allColors["darkWine"], command=self.clear_button)
        self.buttonEquals = CTkButton(self, text="=", corner_radius=5, width=170, height=40, bg_color=allColors["mountbatten"], fg_color=allColors["feldgrau"], hover_color=allColors["darkFeldgrau"], command=self.equals_button)

        #putting everything in view
        self.createView()

        #calculator stack
        self.numbers = []
        self.operators = []

    
    def createButtons(self):
        self.buttons = []
        for i in range(3, 0, -1):
            for j in range(1, 4):
                num = i * 3 - 3 + j
                self.buttons.append(CTkButton(self, text=num, corner_radius=5, bg_color=allColors["mountbatten"], fg_color=allColors["lavender"], text_color=allColors["black"], hover_color=allColors["darkLavender"], width=80, height=40, command=lambda num=num: self.num_buttons(num)))
        self.buttons.append(CTkButton(self, text=0, corner_radius=5, bg_color=allColors["mountbatten"], fg_color=allColors["lavender"], text_color=allColors["black"], hover_color=allColors["darkLavender"], width=80, height=40, command=lambda: self.num_buttons(0)))



    def isString(self, *args):
        currentEntry = self.entry.get()

        try:
            float(currentEntry)

        except:
            self.entry.delete(0, END)


    def num_buttons(self, number):
        current = self.entry.get()
        self.entry.delete(0, END)
        self.entry.insert(0, current + str(number))

    
    def add_button(self):
        num = float(self.entry.get())
        self.entry.delete(0, END)
        self.numbers.append(num)
        self.operators.append("+")
    

    def minus_button(self):
        num = float(self.entry.get())
        self.entry.delete(0, END)
        self.numbers.append(num)
        self.operators.append("-")


    def multiply_button(self):
        num = float(self.entry.get())
        self.entry.delete(0, END)
        self.numbers.append(num)
        self.operators.append("*")


    def divide_button(self):
        num = float(self.entry.get())
        self.entry.delete(0, END)
        self.numbers.append(num)
        self.operators.append("/")


    def clear_button(self):
        self.entry.delete(0, END)
        self.numbers = []
        self.operators = []


    def equals_button(self):
        current = float(self.entry.get())
        self.numbers.append(current)
        self.entry.delete(0, END)

        while self.operators:
            num1 = self.numbers.pop(0)
            num2 = self.numbers.pop(0)
            operator = self.operators.pop(0)

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2

            self.numbers.insert(0, result)

        self.entry.insert(0, self.numbers[0])
        self.numbers = []
        self.operators = []


    def createView(self):
                
        #putting the entry widget on the screen
        self.entry.grid(row=0, column=0, columnspan=3, pady=5)

        columns = 3
        for i, button in enumerate(self.buttons):
            row = i // columns + 1
            col = i % columns
            button.grid(row=row, column=col, padx=5, pady=5)

        self.buttonAdd.grid(row=row, column=1, columnspan=2, padx=5, pady=5)

        self.buttonMinus.grid(row=row+1, column=0, padx=5, pady=5)
        self.buttonMultiply.grid(row=row+1, column=1, padx=5, pady=5)
        self.buttonDivide.grid(row=row+1, column=2, padx=5, pady=5)

        self.buttonClear.grid(row=row+2, column=0, padx=5, pady=5)
        self.buttonEquals.grid(row=row+2, column=1, columnspan=2, padx=5, pady=5)
        

    def createView2(self): 

        #create view 

        #this is a test view
        # 
        # for debugging purposes
        pass

        
        


    

        

