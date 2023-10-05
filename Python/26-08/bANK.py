class Bank:
    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("Hello",self.cname,"Your Account Number",self.acno,"Is Opened With",self.balance,"Rs.")
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            self.needs=amount-self.balance
            print("sorry you need anounther",self.needs,"Rs. To Withdraw")
    def checkBalance(self):
        print("Your Current Balance Is :",self.balance)

b1=Bank()
b1.openAccount(102,"Harsh",2000)

while True:

    print("*"*50)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*50)

    choice=int(input("Enter Choice :"))

    if choice==1:
        amount=int(input("Enter Deposit Amount :"))
        b1.deposit(amount)
        print("*"*50)
    elif choice==2:
        amount=int(input("Enter Withdraw Amount :"))
        b1.withdraw(amount)
        print("*"*50)
    elif choice==3:
        b1.checkBalance()
        print("*"*50)
    elif choice==4:
        print("Thank You For USing Our Service.Good Bye")
        print("*"*50)
        break
    else:
        print("Invalid Choice. Try Again")
        
