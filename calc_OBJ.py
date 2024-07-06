import tkinter as tk
from tkinter import ttk

class Calculator:


    def __init__(self,window):
        self.window = window
        self.window.title("Calculadora Orientada a Objetos")
        self.window.config(width=400, height=300, bg='#cacaca')

        self.create_widgets()

    def create_widgets(self):
        #valor1
        self.tag_value1 = ttk.Label(self.window, text="Valor 1: ")
        self.tag_value1.place(x=20, y=20)

        #caja1
        self.box_value1 = ttk.Entry(self.window)
        self.box_value1.place(x=80, y=20, width=60)

        #VALOR2
        self.tag_value2 = ttk.Label(self.window, text="Valor 2: ")
        self.tag_value2.place(x=20, y=60)

        #caja2
        self.box_value2 = ttk.Entry(self.window)
        self.box_value2.place(x=80, y=60, width=60)

        #boton resolver
        self.button_solve = ttk.Button(self.window, text="Resolver", command= self.show_solution )
        self.button_solve.place(x=20, y=180)

        #resultado
        self.tag_solve = ttk.Label(self.window, text= "Resultado: ")
        self.tag_solve.place(x=20, y=100)

        #cajasolucion
        self.box_solve = ttk.Entry(self.window, )
        self.box_solve.place(x=80, y=100, width=60)

        #boton salida
        self.button_exit = ttk.Button(self.window, text="Salir", command= self.window.quit)
        self.button_exit.pack()
        self.button_exit.place(x=340, y=270, width=60)
        #almaceno opcion
        self.option= tk.StringVar(value="")

        #botones de opcion
        self.addittion=ttk.Radiobutton(text="Sumar",vari= self.option, value="1")
        self.addittion.place(x=20, y=140, width=60)
        self.substraction=ttk.Radiobutton(text="Restar", vari= self.option, value="2")
        self.substraction.place(x=80, y=140, width=60)
        self.multiply=ttk.Radiobutton(text="Multiplicar", vari= self.option, value="3")
        self.multiply.place(x=140, y=140, width=80)
        self.divide=ttk.Radiobutton(text="Dividir", vari= self.option, value="4")
        self.divide.place(x=220, y=140, width=60)

    def add_solve(self,val1,val2):
        return val1 + val2
    def sub_solve(self,val1,val2):
        return val1 - val2
    def mul_solve(self,val1,val2):
        return val1 * val2
    def div_solve(self,val1,val2):
        return val1 / val2
    
    def select_option(self, *args):
        print(f"Operacion Selecciondada: {self.option.get()}")

    def show_solution(self):
        try:
            val1 = float(self.box_value1.get())
            val2 = float(self.box_value2.get())
            op = self.option.get()

            operation ={
                    "1":self.add_solve,
                    "2":self.sub_solve,
                    "3":self.mul_solve,
                    "4":self.div_solve
            }   

            if op in operation:
                result = operation[op](val1,val2)
        
                self.box_solve.delete(0, tk.END)
                self.box_solve.insert(0, str(result))
       
        except    ValueError:
            self.box_solve.delete(0, tk.END)
            self.box_solve.insert(0,"Error")   

if __name__=="__main__":
    window=tk.Tk()
    app=Calculator(window)
    window.mainloop()

