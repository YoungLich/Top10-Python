import tkinter as tk

def calcular():
    try:
        resultado.set(eval(entrada.get()))
    except Exception as e:
        resultado.set("Erro")

root = tk.Tk()
root.title("Calculadora")

entrada = tk.Entry(root, width=16, font=("Arial", 24))
entrada.grid(row=0, column=0, columnspan=4)

resultado = tk.StringVar()
lbl_resultado = tk.Label(root, textvariable=resultado, font=("Arial", 24))
lbl_resultado.grid(row=1, column=0, columnspan=4)

botoes = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']

row = 2
col = 0
for botao in botoes:
    cmd = lambda b=botao: entrada.insert(tk.END, b) if b != '=' else calcular()
    tk.Button(root, text=botao, command=cmd, font=("Arial", 18)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="C", command=lambda: entrada.delete(0, tk.END), font=("Arial", 18)).grid(row=row, column=0, columnspan=4)
root.mainloop()
