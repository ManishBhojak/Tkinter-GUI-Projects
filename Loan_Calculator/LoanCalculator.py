from tkinter import * #Import the tkinter module

class LoanCalculator: #created a class named Loancalculator
    def __init__(self): #defining the initializing Function in the class
        #Defining root window of the application
        window=Tk()
        window.title('Loan Calculator') #title of the application
        window.configure(bg='lime') #background color for the application
        
        #Create the labels
        Label(window,text='Annual Interest Rate: ',bg='lime',font='Arial 12 bold').grid(row=1,column=1,sticky=W)
        Label(window,text='Number of Years: ',bg='lime',font='Arial 12 bold').grid(row=2,column=1,sticky=W)
        Label(window,text='Loan Amount: ',bg='lime',font='Arial 12 bold').grid(row=3,column=1,sticky=W)
        Label(window,text='Monthly Payment: ',bg='lime',font='Arial 12 bold').grid(row=4,column=1,sticky=W)
        Label(window,text='Total Payment: ',bg='lime',font='Arial 12 bold').grid(row=5,column=1,sticky=W)
        
        #Created the TextField and String Variable Values
        self.interestRateVar = StringVar()
        Entry(window,font='Arial 12 bold',textvariable=self.interestRateVar,justify=RIGHT).grid(row=1,column=2,pady=12)
        self.numofYearsVar = StringVar()
        Entry(window,textvariable=self.numofYearsVar,font='Arial 12 bold',justify=RIGHT).grid(row=2,column=2,pady=12)
        self.loanAmountVar = StringVar()
        Entry(window,textvariable=self.loanAmountVar,font='Arial 12 bold',justify=RIGHT).grid(row=3,column=2,pady=12)
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment=Label(window,textvariable=self.monthlyPaymentVar,font='Arial 12 bold',bg='lime',fg='red').grid(row=4,column=2,sticky=E,pady=12)
        self.totalPaymentVar =StringVar()
        lblTotalPayment=Label(window,textvariable=self.totalPaymentVar,font='Arial 12 bold',bg='lime',fg='red').grid(row=5,column=2,sticky=E,pady=12)
        
        #Creating Buttons Compute Payment and Clear to Perform Calculation function and Clear the Value
        btnComputePayment=Button(window,text='Compute Payment',bg='red',fg='white',font='Helvatica 14',command=self.computedAmount).grid(row=6,column=2)
        btnClearAll=Button(window,text='Clear',bg='blue',fg='white',font='Helvatica 14',command=self.deleteAll).grid(row=6,column=3,padx=25,pady=30)
        
        window.mainloop()
    
    #Defining computedAmount and deleteAll function to perform working of buttons in application    
    def computedAmount(self):
        monthlyPayment = self.getMonthlyPayment(float(self.loanAmountVar.get()),
                                                float(self.interestRateVar.get())/1200,
                                                int(self.numofYearsVar.get()))
        self.monthlyPaymentVar.set(format(monthlyPayment,'10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get())*12 \
            * int(self.numofYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment,'10.2f'))
        
    #Defining getMonthlyPayment function call in between computedAmount function to function the command
    def getMonthlyPayment(self,loanAmount,monthlyInterestRate,NumOfyears):
        monthlyPayment = loanAmount * monthlyInterestRate/ (1-1/(1+monthlyInterestRate)** (NumOfyears*12))
        return monthlyPayment
    
    def deleteAll(self):
        self.interestRateVar.set("")
        self.numofYearsVar.set("")
        self.loanAmountVar.set("")
        self.monthlyPaymentVar.set("")
        self.totalPaymentVar.set("")



LoanCalculator()
