class Student:
    def getData (self,fname,lname):
        print("getData Called")
        self.f=fname
        self.l=lname
    def putData(self):
        print("putData Called")
        print("first NAme :",self.f)
        print("last NAme :",self.l)

s1=Student()
s1.getData("Harsh","Deep")
s1.putData()
