import requests
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



category =[ "life expenses", "electricity", "gas", "rental", "grocery", "savings", "education", "charity"]
payment_type=["Cash", "Credit Card", "Paypal"]

expense = []
colums=('DateTime','Amount','Currency','Category','Type','  ')

window=tk.Tk()
window.title("Bahgat Expense Traker")

amolist =[]

def get_total_expense():
    amolist.clear()  
    for x in expense:
       if x[2] !="USD":
            convert_to_dollar()      
       else:
            amolist.append(float(x[1]))
    totalamount=sum(amolist)
    total_box.config(text = totalamount )



def reset_entery():
    ammount_box.delete("1.0","end")
    currencyvariabk.set("   ")
    categoryvariable.set("   ")
    payvaiable.set("   ")



def show_expense_history():
    for item in data_history_tree.get_children():
        data_history_tree.delete(item)
    for line in expense:
      data_history_tree.insert('', tk.END, values=line)
      
def convert_to_dollar():
  
        url = "https://api.apilayer.com/fixer/convert?"
        headers= { "apikey": "EjZVCxmKAVdgQLH63EoLkFw842vHXyMj" }
        parameter = {
                    "to" :   "USD"  ,
                    "from": currencyvariabk.get() ,
                    "amount" : ammount_box.get(1.0, "end-1c")}
        response = requests.request("GET", url, headers=headers, params=parameter )
        result = response.json()['result']
        amolist.append(float(result))
   

def add_new_expense():
    DATE=datetime.datetime.now()
    ADMOUNT=ammount_box.get(1.0,"end-1c")
    ADCUURENCY=currencyvariabk.get()
    ADCATEGORY=categoryvariable.get()
    ADPAYTYPE = payvaiable.get()
    expense.append([DATE,ADMOUNT,ADCUURENCY,ADCATEGORY,ADPAYTYPE])


    show_expense_history()
    get_total_expense()
    reset_entery()

 


#ui 
#main fraims
expens_history_frame=tk.Frame()
data_entry_frame=tk.Frame()

expens_history_frame.rowconfigure(0)
data_entry_frame.rowconfigure(2)

expens_history_frame.grid(row=0,column=0,sticky="NW")
data_entry_frame.grid(row=1,column=0,sticky="NW")

#frames  component
ammount_box=tk.Text(data_entry_frame,height=1,width=8)
ammount_box.grid(column=1,row=0,sticky="EW")
ammount_box_LABEL=ttk.Label(data_entry_frame,text="Amount")
ammount_box_LABEL.grid(row=0,column=0,sticky="N")



total_label=tk.Label(expens_history_frame,text="Total")
total_label.grid(row=1,column=0,sticky="NW",pady=5)

total_box=tk.Label(expens_history_frame,text="0",font=("Arial", 15) )
total_box.grid(row=1,column=0,sticky="N",pady=5)


currencyvariabk=tk.StringVar()
categoryvariable=tk.StringVar()
payvaiable=tk.StringVar()


currency_combobox=ttk.Combobox(data_entry_frame,width=8,values=["USD","EGP"],textvariable=currencyvariabk)
currency_combobox.grid(row=1,column=1,sticky="W")
currency_combobox_LABEL=ttk.Label(data_entry_frame,text="Currency",background="RED")
currency_combobox_LABEL.grid(row=1,column=0,sticky="N")

payment_type_combbox=ttk.Combobox(data_entry_frame,width=8,values=payment_type,textvariable=payvaiable)
payment_type_combbox.grid(row=2,column=1,sticky="SW")
payment_type_combbox_label=ttk.Label(data_entry_frame,text="Pay Type")
payment_type_combbox_label.grid(row=2,column=0,sticky="N")





category_comobox=ttk.Combobox(data_entry_frame,width=8,values=category,textvariable=categoryvariable)
category_comobox.grid(row=0,column=3,sticky="NE")
category_comobox_label=ttk.Label(data_entry_frame,text="Category")
category_comobox_label.grid(row=0,column=2,sticky="N")

datetime_box =tk.Label(data_entry_frame,text= datetime.datetime.now(),height=1,width=6)               
datetime_box.grid(row=1,column=3,sticky="NE")
datetime_box_label=ttk.Label(data_entry_frame,text="Date")
datetime_box_label.grid(row=1,column=2,sticky="N")






enter_button=tk.Button(data_entry_frame,text="Enter",width=5,height=2,relief="raised",fg="GREEN", bg='RED',border=2,command= add_new_expense)
enter_button.grid(row=0,column=4,rowspan=2,sticky="EW")



data_history_tree=ttk.Treeview(expens_history_frame,columns=colums,show='headings')
data_history_tree.grid(row=0,column=0,sticky="NW")
data_history_tree.heading('DateTime', text='Date Time')
data_history_tree.column("DateTime",minwidth=0,width=100) 
data_history_tree.heading('Amount', text='Amount')
data_history_tree.column("Amount",minwidth=0,width=100) 
data_history_tree.heading('Currency', text='Currency')
data_history_tree.column("Currency",minwidth=0,width=100) 
data_history_tree.heading('Category', text='Category')
data_history_tree.column("Category",minwidth=0,width=100) 
data_history_tree.heading('Type', text='Type')
data_history_tree.column("Type",minwidth=0,width=100) 
data_history_tree.heading('  ', text='  ')
data_history_tree.column("  ",minwidth=0,width=10) 





window.mainloop()

