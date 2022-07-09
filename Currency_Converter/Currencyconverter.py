import tkinter as tk
from tkinter import *
from tkinter import messagebox

CurrencyCodesList = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]



root = tk.Tk()
root.configure(background="#e6e5e5")
root.title("Currency Converter")
root.geometry("700x400")


variable1 = tk.StringVar(root)
variable1.set('currency')
variable2 = tk.StringVar(root)
variable2.set('currency')

frame = LabelFrame(root, bg = '#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
frame.grid(row=0,column=1,padx=8,pady=8,sticky='ew')

Label_1 = Label(frame, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=1, column=0, sticky=W,padx=2)

label1=Label(frame,font=('lato black',15,'bold'),text="Amount: ",padx=2,pady=2,bg="#e6e5e5",fg='black')
label1.grid(row=4,column=0,sticky=W,padx=2)
label1=Label(frame,font=('lato black',15,'bold'),text="From Currency: ",padx=2,pady=2,bg="#e6e5e5",fg='black')
label1.grid(row=2,column=0,sticky=W,padx=2)
label1=Label(frame,font=('lato black',15,'bold'),text="To Currency: ",padx=2,pady=2,bg="#e6e5e5",fg='black')
label1.grid(row=6,column=0,sticky=W,padx=2)
label1=Label(frame,font=('lato black',15,'bold'),text="Conveted Amount: ",padx=2,pady=2,bg="#e6e5e5",fg='black')
label1.grid(row=8,column=0,sticky=W,padx=2)

Label_1 = Label(frame, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=5, column=0, sticky=W)
Label_1 = Label(frame, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=7, column=0, sticky=W)

from_curr_option = OptionMenu(frame,variable1, *CurrencyCodesList).grid(row=2,column=1,ipadx=45,sticky=E)
to_curr_option = OptionMenu(frame,variable2, *CurrencyCodesList).grid(row=6,column=1,ipadx=45,sticky=E)

amtField1 = Entry(frame)
amtField1.grid(row=4,column=1,ipadx=28,sticky=E)
amtField2 = Entry(frame)
amtField2.grid(row=8,column=1,ipadx=31,sticky=E)

def real_timeCurrencyConverter():
    from forex_python.converter import CurrencyRates
    currRates = CurrencyRates()
    
    from_currency = variable1.get()
    to_currency = variable2.get()
    
    if (amtField1.get()==""):
        messagebox.showinfo("Error !!","Please Enter a Amount")
    elif (from_currency == "currency" or to_currency == "currency"):
        messagebox.showinfo("Error !!","Currency Not Selected")
    else:
        newAmt = currRates.convert(from_currency,to_currency,float(amtField1.get()))
        new_amount = float("{:.2f}".format(newAmt))
        amtField2.insert(0,str(newAmt))
    
def clear():
    amtField1.delete(0, tk.END)
    amtField2.delete(0, tk.END)

convbtn = Button(frame,font=('Arial',12,"bold"),text='Convert',padx=2,pady=2,bg='blue',fg='white',command=real_timeCurrencyConverter)
convbtn.grid(row=12,column=0,ipady=2,pady=5)
clearbtn = Button(frame,font=('Arial',12,"bold"),text='Clear All',padx=2,pady=2,bg='Red',fg='white',command=clear)
clearbtn.grid(row=12,column=1,ipady=2,pady=5)
root.mainloop()
