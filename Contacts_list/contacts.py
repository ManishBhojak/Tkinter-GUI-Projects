#import Tkinter module
from logging import root
from tkinter import Tk, Button, PhotoImage,Label,LabelFrame,W,E,N,S,Entry,END,StringVar,Scrollbar,Toplevel
from tkinter import ttk #provides access to the themed widgets
import sqlite3


class Contacts:
    #importing database file
    db_filename='contacts.db'
    
    def __init__(self,root):
        self.root = root
        self.create_gui()
       
    #Connecting Sqlite Database
    def database_connection(self,query,parameters=()):
        with sqlite3.connect(self.db_filename) as conn:
            print(conn)
            print('You have Successfully connected to Database')
            cursor =conn.cursor()
            query_result = cursor.execute(query,parameters)
            conn.commit()
        return query_result
    
    #Adding Function for GUI
    def create_gui(self):
        self.create_icon()
        self.create_label_frame()
        self.create_message_area()
        self.create_treeview()
        self.create_scrollbar()
        self.create_bottom_buttons()
        self.view_contacts()
        
        #Styling the treeview 
        ttk.style = ttk.Style()
        ttk.style.configure('Treeview', font=('Times New Roman',12))
        ttk.style.configure('Treeview.Heading',font=('Times New Roman',12,'bold'))
        
    #Add Logo to an Application
    def create_icon(self):
        photo= PhotoImage(file='icons/logo.gif')
        label= Label(image=photo)
        label.image =photo
        label.grid(row=0, column=0)
        
    #Create Label Frame    
    def create_label_frame(self):
        labelframe=LabelFrame(self.root,text='Create New Contact', bg='sky blue', font=('Times New Roman',12,'bold'))
        labelframe.grid(row=0,column=1,padx=8,pady=8,sticky='ew')
        
    #Add labels, TextFields and Button
        Label(labelframe, text='Name:',bg='yellow',fg='red').grid(row=1,column=1,sticky=W,pady=2,padx=15)
        self.namefield= Entry(labelframe)
        self.namefield.grid(row=1,column=2,sticky=W,padx=5,pady=2)
        Label(labelframe, text='E-mail:',bg='yellow',fg='red').grid(row=2,column=1,sticky=W,pady=2,padx=15)
        self.emailfield= Entry(labelframe)
        self.emailfield.grid(row=2,column=2,sticky=W,padx=5,pady=2)
        Label(labelframe, text='Number:',bg='yellow',fg='red').grid(row=3,column=1,sticky=W,pady=2,padx=15)
        self.numfield= Entry(labelframe)
        self.numfield.grid(row=3,column=2,sticky=W,padx=5,pady=2)
        Button(labelframe,text='Add Contact',command=self.on_add_contact_button_clicked,bg='blue',fg='white', font=('Arial',9,'bold')).grid(row=4,column=2,sticky=E,padx=5,pady=5)
    
    #Add Message Block
    def create_message_area(self):
        self.message = Label(text='', fg='red')
        self.message.grid(row=3,column=1,sticky=W)
    
    #Add TreeView Block
    def create_treeview(self):
        self.tree = ttk.Treeview(height=10,columns=('email','number'))
        self.tree.grid(row=6,column=0,columnspan=3)
        self.tree.heading('#0',text='Name',anchor=W)
        self.tree.heading('email',text='Email Address',anchor=W)
        self.tree.heading('number',text='Contact Number',anchor=W)
    
    #Add ScrollBar to TreeView
    def create_scrollbar(self):
        self.scrollbar = Scrollbar(orient='vertical',command=self.tree.yview)
        self.scrollbar.grid(row=6,column=3,rowspan=10,sticky='sn')
        
    #Adding Some more Buttons
    def create_bottom_buttons(self):
        Button(text='Delete Contact',command=self.on_delete_selected_button_clicked,bg='orange',fg='blue',font=('Arial',9,'bold')).grid(row=8,column=0,sticky=W,pady=10,padx=20)
        Button(text='Modify Contact',command=self.on_modify_selected_button_clicked,bg='orange',fg='blue',font=('Arial',9,'bold')).grid(row=8,column=1,sticky=W,pady=10,padx=20)
        
    #Add add_contact function on Button
    def on_add_contact_button_clicked(self):
        self.add_new_contact()
    
    #add delete Button Function
    def on_delete_selected_button_clicked(self):
        self.message['text']=''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text']='No item selected to delete'
            return
        self.delete_contacts()
     
    #add Update Button Function   
    def on_modify_selected_button_clicked(self):
        self.message['text']=''
        try:
            self.tree.item(self.tree.selection())['values'][0]
            
        except IndexError as e:
            self.message['text']='No item selected to modify'
            return
        self.modify_window()  
                  
    #Add function for Adding an Contact to the Database
    def add_new_contact(self):
        if self.new_contact_validate():
            query='INSERT INTO contact_list VALUES(NULL,?,?,?)'
            parameters = (self.namefield.get(),self.emailfield.get(),self.numfield.get())
            self.database_connection(query,parameters)
            self.message['text']= 'New Contact {} added'.format(self.namefield.get())
            self.namefield.delete(0,END)
            self.emailfield.delete(0,END)
            self.numfield.delete(0,END)
        else:
            self.message['text']='Name,Email and Contact Number cannot be Blank!'
        self.view_contacts()
        
    def new_contact_validate(self):
        return len(self.namefield.get()) !=0 and len(self.emailfield.get()) !=0 and len(self.numfield.get()) !=0
    
    def view_contacts(self):
        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        query = 'SELECT * FROM contact_list ORDER BY name desc'
        contact_entries = self.database_connection(query)
        for row in contact_entries:
            self.tree.insert('',0,text=row[1],values=(row[2],row[3]))
    
    #Add Delete Contact Button code
    def delete_contacts(self):
        self.message['text']=''
        name=self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM contact_list WHERE name=?'
        self.database_connection(query,(name,))
        self.message['text'] = 'Contact for {} deleted'.format(name)
        self.view_contacts()
    
    #Create New popup Update Contact Window
    def modify_window(self):
        name=self.tree.item(self.tree.selection())['text']
        old_number= self.tree.item(self.tree.selection())['values'][1]
        self.transient=Toplevel()
        self.transient.title('Update Contact')
        Label(self.transient,text='Name: ').grid(row=0,column=1)
        Entry(self.transient,textvariable=StringVar(self.transient,value=name),state='readonly').grid(row=0,column=2)
        Label(self.transient,text='Old Contact Number: ').grid(row=1,column=1)
        Entry(self.transient,textvariable=StringVar(self.transient,value=old_number),state='readonly').grid(row=1,column=2)
        
        Label(self.transient,text='New Contact Number: ').grid(row=2,column=1)
        new_phone_number=Entry(self.transient)
        new_phone_number.grid(row=2,column=2)
        
        Button(self.transient,text='Update Contact',bg='blue',fg='white',command=lambda: self.update_contact(new_phone_number.get(),old_number,name)).grid(row=3,column=2,sticky=E)
        
        self.transient.mainloop()
        
    #Create Function for Update an Contact
    def update_contact(self,newphone,old_phone,name):
        query='UPDATE contact_list SET number=? WHERE number=? AND name=?'
        parameters=(newphone,old_phone,name)
        self.database_connection(query,parameters)
        self.transient.destroy()
        self.message['text']='Phone Number of {} modified'.format(name)
        self.view_contacts()

#Main Method of the Class
if __name__ == '__main__':
    root=Tk()
    root.title('My Contact Details')
    root.geometry('650x450')
    root.resizable(width=False,height=False)
    application = Contacts(root)
    root.mainloop()
    
    #Code Ends Here!!! 
