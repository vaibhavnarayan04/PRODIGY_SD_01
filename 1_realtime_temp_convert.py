
#TASK 1

from tkinter import *

def from_fahrenheit(*args):
    try:
        f = float(fahrenheit_var.get())
        c = (f - 32) * 5/9
        k = c + 273.15
        updating[0] = True
        celsius_var.set(f"{c:.2f}")
        kelvin_var.set(f"{k:.2f}")
        updating[0] = False
    except:
        if not updating[0]:
            celsius_var.set("")
            kelvin_var.set("")

def from_celsius(*args):
    try:
        c = float(celsius_var.get())
        f = (c * 9/5) + 32
        k = c + 273.15
        updating[0] = True
        fahrenheit_var.set(f"{f:.2f}")
        kelvin_var.set(f"{k:.2f}")
        updating[0] = False
    except:
        if not updating[0]:
            fahrenheit_var.set("")
            kelvin_var.set("")

def from_kelvin(*args):
    try:
        k = float(kelvin_var.get())
        c = k - 273.15
        f = (c * 9/5) + 32
        updating[0] = True
        celsius_var.set(f"{c:.2f}")
        fahrenheit_var.set(f"{f:.2f}")
        updating[0] = False
    except:
        if not updating[0]:
            fahrenheit_var.set("")
            celsius_var.set("")

Root = Tk()
Root.title("Temperature Converter")
Root.geometry("400x250")
Root.resizable(0, 0)

updating = [False]

# Define StringVars
fahrenheit_var = StringVar()
celsius_var = StringVar()
kelvin_var = StringVar()

fahrenheit_var.trace_add('write', from_fahrenheit)
celsius_var.trace_add('write', from_celsius)
kelvin_var.trace_add('write', from_kelvin)

# Fahrenheit
Label(Root, text='Fahrenheit:', font='Arial 12').grid(row=0, column=0, padx=10, pady=10)
Entry(Root, font=('Arial', 12), textvariable=fahrenheit_var).grid(row=0, column=1)

# Celsius
Label(Root, text='Celsius:', font='Arial 12').grid(row=1, column=0, padx=10, pady=10)
Entry(Root, font=('Arial', 12), textvariable=celsius_var).grid(row=1, column=1)

# Kelvin
Label(Root, text='Kelvin:', font='Arial 12').grid(row=2, column=0, padx=10, pady=10)
Entry(Root, font=('Arial', 12), textvariable=kelvin_var).grid(row=2, column=1)

Root.mainloop()