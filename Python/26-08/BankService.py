class BankService:
    def welcome(self,cname,balance):
        self.cname=cname
        self.balance=balance
        print("Hello ",self.cname,", Welcome to our services!")
        print("Your account has balance Rs.",self.balance)
    def creditcard(self,cno,amount,mobileno):
        self.cno=cno
        self.amount=amount
        self.mobileno=mobileno
        print("Your card number-",self.cno,"credit card balance Rs.",self.amount,"Your Mobile Number is :",mobileno)
    def dabitcard(self,cno,amount,mobileno):
        self.cno=cno
        self.amount=amount
        self.mobileno=mobileno
        print("Your card number-",self.cno,"dabit card balance Rs.",self.amount,"Your Mobile Number is :",mobileno)
    def internetbanking(self,ano,amount,mobileno):
        self.ano=ano
        self.amount=amount
        self.mobileno=mobileno
        print("Your account number-",self.ano,"will be transaction amount Rs.",self.amount,"Your Mobile Number is :",mobileno)
    def help(self,tranproblem,accountproblem):
        self.tranproblem=tranproblem
        self.accountproblem=accountproblem
        print("Your transaction problem is:",tranproblem)
        print("Your Account Problem is:",accountproblem)
b1=BankService()
b1.welcome("Harshdeep",50000)

while True:
    print("*"*50)
    print("1.Credit Card\n2.Debit Card\n3.Internet Banking\n4.Help\n5.Exit")
    print("*"*50)
    choice=int(input("Enter choice:"))
    print("*"*50)
    if choice==1:
        cno=int(input("Enter card number:"))
        amount=int(input("Enter amount:"))
        mobileno=int(input("Enter Mobile Number: "))
        b1.creditcard(cno,amount,mobileno)
        print("*"*50)
    elif choice==2:
        cno=int(input("Enter card number:"))
        amount=int(input("Enter amount:"))
        mobileno=int(input("Enter Mobile Number: "))
        b1.dabitcard(cno,amount,mobileno)
        print("*"*50)
    elif choice==3:
        ano=int(input("Enter card number:"))
        amount=int(input("Enter amount:"))
        mobileno=int(input("Enter Mobile Number: "))
        b1.internetbanking(ano,amount,mobileno)
        print("*"*50)
    elif choice==4:
        tranproblem=input("Enter Transaction Problem")
        accountproblem=input("Enter Account Problem")
        b1.help(tranproblem,accountproblem)
        print("*"*50)
    elif choice==5:
        print("Thank You for using our services , Good Bye!")
        print("*"*50)
        break
    else:
        print("Invalid choice!")
        print("*"*50)
