import tkinter as tk
from tkinter import ttk

def add_solve(val1,val2):
    return val1 + val2
def sub_solve(val1,val2):
    return val1 - val2
def mul_solve(val1,val2):
    return val1 * val2
def div_solve(val1,val2):
    return val1 / val2

operation ={
    "1":add_solve,
    "2":sub_solve,
    "3":mul_solve,
    "4":div_solve
}

def show_solution():
    try:
        val1 = float(box_value1.get())
        val2 = float(box_value2.get())
        op = option.get()

        if op in operation:
            result = operation[op](val1,val2)
        
        box_solve.delete(0, tk.END)
        box_solve.insert(0, str(result))
       
    except    ValueError:
        box_solve.delete(0, tk.END)
        box_solve.insert(0,"Error")    

window = tk.Tk()
window.title("Calculadora Paradigma Estructurado")
window.config(width=400, height=300, bg ='#cacaca')
#valor1
tag_value1 = ttk.Label(text="Valor 1: ")
tag_value1.place(x=20, y=20)

#caja1
box_value1 = ttk.Entry()
box_value1.place(x=80, y=20, width=60)

#VALOR2
tag_value2 = ttk.Label(text="Valor 2: ")
tag_value2.place(x=20, y=60)

#caja2
box_value2 = ttk.Entry()
box_value2.place(x=80, y=60, width=60)

#boton resolver
button_solve = ttk.Button(text="Resolver", command= show_solution )
button_solve.place(x=20, y=180)

#resultado
tag_solve = ttk.Label(text= "Resultado: ")
tag_solve.place(x=20, y=100)

#cajasolucion
box_solve = ttk.Entry()
box_solve.place(x=80, y=100, width=60)

#boton salida
button_exit = ttk.Button(window, text="Salir", command= exit)
button_exit.pack()
button_exit.place(x=340, y=270, width=60)

#calculos
def select_opt():
    select= option.get()

#almaceno opcion
option= tk.StringVar(value="")

#botones de opcion
addittion=ttk.Radiobutton(text="Sumar",vari= option, value="1")
addittion.place(x=20, y=140, width=60)
substraction=ttk.Radiobutton(text="Restar", vari= option, value="2")
substraction.place(x=80, y=140, width=60)
multiply=ttk.Radiobutton(text="Multiplicar", vari= option, value="3")
multiply.place(x=140, y=140, width=80)
divide=ttk.Radiobutton(text="Dividir", vari= option, value="4")
divide.place(x=220, y=140, width=60)


window.mainloop()