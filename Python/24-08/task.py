file=open("Exception.txt","w")
s="this is Exception Heandling"
try:
    t=int(input("Enter t: "))
    k=s*t
    file.write(k)
except Exception as e:
    print("Excepation Caught :",e)

finally:
    file.close()
    
    
