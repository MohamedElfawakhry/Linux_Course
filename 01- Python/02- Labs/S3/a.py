
import os 
name = input("Enter Your Name : ")
age = input ("Enter Your Age : ")
college = input("Enter Your department ")

f1 = open("file1.txt","w+")
f1.write("Name is : "+name+"\n")
f1.write("Age  is : "+age+"\n")
f1.write("Department is : "+college)

f1=open("file1.txt", "r")
#print(f1.read())
print(f1.readlines(18))
f1.close()
os.remove("file1.txt")