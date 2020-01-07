import cmsoplist
from tkinter import *
from tkinter import messagebox

def btnAdd_click():
    cus = cmsoplist.Customer()
    cus.id = varId.get()
    cus.age = varAge.get()
    cus.name = varName.get()
    cus.addCustomer()
    varId.set("")
    varAge.set("")
    varName.set("")
    messagebox.showinfo("CMS","customer added successfully")

def btnSrch_click():
    cus = cmsoplist.Customer()
    cus.id = varId.get()
    cus.searchCustomer()
    varAge.set(cus.age)
    varName.set(cus.name)
    messagebox.askyesno("CMS","customer searched,want to continue?")
    varId.set("")
    varAge.set("")
    varName.set("")

def btnDel_click():
    id = varId.get()
    cmsoplist.Customer.deleteCustomer(id)
    messagebox.showinfo("CMS","customer deleted successfully")
    varId.set("")
    varAge.set("")
    varName.set("")

def btnDisplayAll_click():
    root1 = Tk()
    count = 0
    root1.geometry("400x400")
    for  e in cmsoplist.Customer.listCus:
        count += 1
        lblId1 = Label(root1,text=e.id,height=2,width=10,bg="red")
        lblId1.grid(row=count,column=0)

        lblAge1 = Label(root1, text=e.age, height=2, width=10, bg="red")
        lblAge1.grid(row=count, column=1)

        lblName1 = Label(root1, text=e.name, height=2, width=10, bg="red")
        lblName1.grid(row=count, column=2)

    root1.mainloop()






root = Tk()

root.geometry("500x300")
root.state("zoomed")



lblId = Label(root,text="enter id:",width = 20,height = 2,font = 14)
lblId.grid(row=0,column=0)

varId = StringVar()

entrId = Entry(root,textvariable=varId)
entrId.grid(row=0,column=1)



lblAge = Label(root,text="enter age",width = 20,height = 2,font = 14)
lblAge.grid(row=1,column=0)

varAge = StringVar()

entrId = Entry(root,textvariable=varAge)
entrId.grid(row=1,column=1)


lblName = Label(root,text="enter name",width = 20,height = 2,font = 14)
lblName.grid(row=2,column=0)

varName = StringVar()

entrName = Entry(root,textvariable=varName)
entrName.grid(row=2,column=1)


btnAdd = Button(root,text="Add Customer",height=20,font=14,command=btnAdd_click) #command m function pointer or address dete h
btnAdd.grid(row=4,column=0)

btnDel = Button(root,text="Delete Customer",height=20,font=14,command=btnDel_click)
btnDel.grid(row=4,column=1)

btnSrch = Button(root,text="Search Customer",height=20,font=14,command=btnSrch_click)
btnSrch.grid(row=4,column=2)

btnDisplayAll = Button(root,text="Display all Customer",height=20,font=14,command=btnDisplayAll_click)
btnDisplayAll.grid(row=4,column=3)

root.mainloop()



