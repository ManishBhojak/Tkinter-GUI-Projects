from tkinter import *

class currencyConverter:
    def __init__(self):
        window=Tk()
        window.title('Currency Converter')
        window.configure(bg="blue")
        Label(window,font='Helvatica 14 bold',text='Amount to Convert: ',bg='blue',fg='white').grid(row=1,column=1,sticky=W)
        Label(window,font='Helvatica 14 bold',text='Conversion Rate: ',bg='blue',fg='white').grid(row=2,column=1,sticky=W)
        Label(window,font='Helvatica 14 bold',text='Converted Amount: ',bg='blue',fg='white').grid(row=3,column=1,sticky=W)
        self.amounttoconvertVar = StringVar()
        Entry(window,textvariable=self.amounttoconvertVar,justify=RIGHT).grid(row=1,column=2)
        self.conversionrateVar = StringVar()
        Entry(window,textvariable=self.conversionrateVar,justify=RIGHT).grid(row=2,column=2)
        self.convertedamountVar = StringVar()
        ConvertedAmount=Label(window,font='Helvatica 14 bold',bg='blue',fg='white',textvariable=self.convertedamountVar).grid(row=3,column=2,sticky=E)
        
        #Creating the Convert and Clear Button for my Application
        btnConvertedAmount=Button(window,text='Convert',font='Helvatica 16 bold',bg="green",fg='white',command=self.convertAmount).grid(row=4,column=2,sticky=E)
        btnClearAmount=Button(window,text='Clear',font='Helvatica 16 bold',bg="red",fg='white',command=self.clearAmount).grid(row=4,column=3,padx=25,pady=25,sticky=E)
        
        window.mainloop()
        
        #Function to do the Conversion stores input and do the conversion
    def convertAmount(self):
        amt=float(self.conversionrateVar.get())
        convertedamountVar=float(self.amounttoconvertVar.get())*amt
        self.convertedamountVar.set(format(convertedamountVar,'10.2f'))
        #Function to Clear the Values inputed
    def clearAmount(self):
        self.amounttoconvertVar.set("")
        self.conversionrateVar.set("")
        self.convertedamountVar.set("")

currencyConverter()
