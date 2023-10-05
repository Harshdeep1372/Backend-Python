file=open("harsh.txt","w")
s="tis is file management demo"
file.write(s)
file.close()
print("file written sucessfully")
print("*****************************")

file=open("harsh.txt","r")
print(file.read())
file.close()
print("+++++++++++++++++++++++++++++++")

file=open("harsh.txt","a")
file.write("\nThis file is now append")
file.close()
print("******************************")

file=open("harsh.txt","r")
print(file.read())
file.close()
print("*******************************")

file=open("tops2.txt","w+")
file.write("file write operation")
print("file current postion : ",file.tell())
file.seek(0)
print(file.read())
file.close()
print("+++++++++++++++++++++++++++++++++++++++++")

file=open("tops2.txt","r+")
print("Output of the Read function is ")
print(file.read())
print()
  
# The seek(n) takes the file handle to the nth
# byte from the start.
file.seek(0) 
  
print( "The output of the Readline function is ")
print(file.readline()) 
print()
  
file.seek(0)
  
# To show difference between read and readline

print("Output of Read(12) function is ") 
print(file.read(12))
print()

file.seek(0)
  
print("Output of Readline(8) function is ") 
print(file.readline(8))
  
file.seek(0)
# readlines function
print("Output of Readlines function is ") 
print(file.readlines()) 
print()
file.close()
