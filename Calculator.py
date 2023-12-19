import tkinter as tk
from tkinter import ttk
from functools import partial

tempVal = "CELSIUS"

def store_temp(sel_temp):
    global tempVal
    tempVal = sel_temp
	
def call_convert(rlabel1, rlabel2, inputn):
    tem = inputn.get()

    # Check if the input is empty
    if not tem:
        rlabel1.config(text="Please enter a temperature value")
        rlabel2.config(text="")
        return

    try:
        tem_float = float(tem)
    except ValueError:
        rlabel1.config(text="Invalid input. Please enter a valid number.")
        rlabel2.config(text="")
        return

    if tempVal =='CELSIUS':
        if tem_float < -273.15:
            rlabel1.config(text="Temperature is below absolute zero!")
            rlabel2.config(text="")
        else:
            f = float((tem_float * 9/5)+32)
            k = float(tem_float + 273.15)
            rlabel1.config(text="%f FAHRENHEIT" % f)
            rlabel2.config(text="%f KELVIN" % k)
    elif tempVal == 'FAHRENHEIT':
        if tem_float < -459.67:
            rlabel1.config(text="Temperature is below absolute zero!")
            rlabel2.config(text="")
        else:
            c = float((tem_float - 32) *5 /9)
            k = c + 273
            rlabel1.config(text="%f CELSIUS" %c)
            rlabel2.config(text="%f KELVIN" % k)
    elif tempVal == 'KELVIN':
        if tem_float < 0:
            rlabel1.config(text="Temperature is below absolute zero!")
            rlabel2.config(text="")
        else:
            c = float(tem_float - 273.15)
            f = float((tem_float - 273.15) * 1.8000 + 32.00)
            rlabel1.config(text="%f CELSIUS" % c)
            rlabel2.config(text="%f FAHRENHEIT" % f)

root = tk.Tk()
root.geometry('500x250+700+300')
root.title('TEMP CONVERTER')
style = ttk.Style()
root.configure(background='#000000')
root.resizable(width=False, height=False)

style.configure('TNotebook', titlebackground='#09A3BA')

for i in range(7):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

numberInput = tk.StringVar()
var = tk.StringVar()

input_label = tk.Label(root, text="ENTER TEMPERATURE", background='#09A3BA', foreground="#000000")
input_label.grid(row=2, column=1, sticky='e', padx=5, pady=5)
input_entry = tk.Entry(root, textvariable=numberInput, bd=2, relief="solid")
input_entry.grid(row=2, column=2, padx=5, pady=5)

result_label1 = tk.Label(root, background='#09A3BA', foreground="#000000")
result_label1.grid(row=5, column=1, columnspan=5, sticky='nsew', padx=5, pady=5)
result_label2 = tk.Label(root, background='#09A3BA', foreground="#000000")
result_label2.grid(row=6, column=1, columnspan=5, sticky='nsew', padx=5, pady=5)

dropDownList = ["CELSIUS", "FAHRENHEIT", "KELVIN"]
dropdown = tk.OptionMenu(root, var, *dropDownList, command=store_temp)
var.set(dropDownList[0])
dropdown.grid(row=2, column=4, sticky='w', padx=5, pady=5)
dropdown.config(background='#09A3BA', foreground="#000000", bd=2)
dropdown["menu"].config(background='#09A3BA', foreground="#000000")

call_convert = partial(call_convert, result_label1, result_label2, numberInput)
result_button = tk.Button(root, text="CONVERT", command=call_convert, background='#09A3BA', foreground="#000000", bd=2, relief="solid")
result_button.grid(row=4, column=0, columnspan=6, padx=5, pady=5)

root.mainloop()
