#customer management system
#bll
import pickle
import json

class Customer:
    listCus = [] #listcus is a static variable
    def __init__(self):
        self.id = 0
        self.age = 0
        self.name = 0

    def addCustomer(self):
        Customer.listCus.append(self)


    def searchCustomer(self):
        for e in Customer.listCus:
            if(e.id == self.id):
                self.age = e.age
                self.name = e.name
                return 1
        return 0

    @staticmethod
    def deleteCustomer(id):
        for e in Customer.listCus:
            if(e.id == id):
                Customer.listCus.remove(e)

        #for i in range(len(Customer.listcus)):
            #if(Customer.listCus[i].id == id):
                #Customer.listCus.pop(i)

    def modifyCustomer(self):
        for e in Customer.listCus:
            if(e.id == self.id):
                e.age = self.age
                e.name = self.name

    @staticmethod
    def func1(ob):
        return ob.name

    @staticmethod
    def sortData():
        Customer.listCus.sort(key = Customer.func1)

    @staticmethod
    def mysort(L1,pqr):
        for i in range(len(L1)-1):
            for j in range(i+1,len(j)):
                if(pqr(L1[i]) > pqr(L1[j])):
                    L1[i][j] = L1[j][i]

    @staticmethod
    def savetoPickle():
        f = open("C:\\Users\\Dell\\Desktop\\pythoncetpa\\CMSpickle.txt","wb")
        pickle.dump(Customer.listCus,f)
        f.close()

    @staticmethod
    def loadfromPickle():
        f = open("C:\\Users\\Dell\\Desktop\\pythoncetpa\\CMSpickle.txt","rb")
        Customer.listCus = pickle.load(f)
        f.close()

    @staticmethod
    def convtoDict(ob):
        return vars(ob)

    @staticmethod
    def savetoJson():
        f = open("C:\\Users\\Dell\\Desktop\\pythoncetpa\\CMSjson.txt","w")
        json.dump(Customer.listCus,f,default=Customer.convtoDict)
        f.close()


    @staticmethod
    def convtoObj(d):
        cus = Customer()
        cus.id = d["id"]
        cus.age = d["age"]
        cus.name = d["name"]
        return cus

    @staticmethod
    def loadfromJson():
        f = open("C:\\Users\\Dell\\Desktop\\pythoncetpa\\CMSjson.txt","r")
        Customer.listCus = json.load(f,object_hook=Customer.convtoObj)
        f.close()









#pl
def showCustomer(cus):
    print("cusID:",cus.id,"custAge:",cus.age,"custName:",cus.name)


print("welcome to cetpa:CMS")
if(__name__ == "__main__"):
    while(1):
        ch = input("enter choice 1 to 11:"
                   "1 for add,2 for search,3 for modify,4 for delete ,5 for display,6 for exit,7 to sort customer,8 for mysort,9 for save in pickle,10 for load from pickle"
                   ", 11 for save in json,12 for load from json\n")
        if(ch == "1"): #add
                cus = Customer()
                cus.id = input("enter customer's id:")
                cus.age = input("enter customer's age")
                cus.name = input("enter customer's name")
                cus.addCustomer()
                print("customer added successfully.")

        elif(ch == "2"): #search
            cus = Customer()
            cus.id = input("enter customer's id:")
            flag = cus.searchCustomer()
            if(flag == 1):
                showCustomer(cus)
            else:
                print("customer not found")

        elif(ch == "3"): #modify
            cus = Customer()
            cus.id = input("enter cust:ID")
            cus.age = input("enter cus updated age")
            cus.name = input("enter cus updated name")
            cus.modifyCustomer()
            print("customer updated successfully")

        elif(ch == "4"): #delete
            cus = Customer()
            id = input("enter cusID to delete")
            Customer.deleteCustomer(id) #static method ko classname.methodname s call krte hai

        elif(ch == "5"): #display all
            for e in Customer.listCus:
                showCustomer(e)

        elif(ch == "6"): #exit
            break

        elif(ch == "7"): #sort
            Customer.sortData()
            print("customer sorted successfully..")

        elif(ch == "8"):
            Customer.mysort(Customer.listCus,Customer.func1)
            print("sorted..")

        elif(ch == "9"): #save to pickle
            Customer.savetoPickle() #serialization
            print("data saved in pickle  successfully")

        elif(ch == "10"): #load from pickle
            Customer.loadfromPickle() # Deserialization
            print("data loaded from pickle successfully")

        elif(ch == "11"): #save to json
            Customer.savetoJson()
            print("data save in json successfully")

        elif(ch == "12"): #load from json
            Customer.loadfromJson()
            print("data load from json successfuly")

        else:
            print("Incorrect choice")







