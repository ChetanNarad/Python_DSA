#why the python is called as dynamic language
age = 33
pi = 3.14
name = "Prashant"
result = True
Print(type(age))
Print(type(pi))
Print(type(name))
Print(type(result))


#To check the address of variable we use id
age = 33
pi = 3.14
name = "Prashant"
result = True
Print(id(age))
Print(id(pi))
Print(id(name))
Print(id(result))

#why all fundamental datatypes are immutable(non-changeable)
math = 50
chem = 50
physics = 50
print(id(math))
print(id(chem))
print(id(physics))
# It is assign reference value taken from maths to all the variables as it is same


# simple if 
# Input function consider or accept the variable as Default String only

print(2+2) #Give ans 2
print("2"+"2") #Give ans 22
a = input("Enter first Number:")
b = input("Enter Second Number:")
print(a+b)


print(2+2) #Give ans 2
print("2"+"2") #Give ans 22
a = int(input("Enter first Number:"))
b = int(input("Enter Second Number:"))
print(a+b)


#simple if
a = int(input("Enter any single digit:"))
if a>0:
    print("positive number")
    if a<0:
        print("negative number")
        if a==0:
            print("zero")

day = input("Enter your day name :")
if day == "SATURDAY" or day == "saturday" or day =="SUNDAY" or day == "sunday" :
print("weekend")
else:
    print("working day")

    #if else decides the flow of execution and direction of it.

    #if else if
    per = 65
    if per >=65:
        print("grade A")
        elif per <=65 and per>=50:
            print("Grade B")
            else:
                print("Fail")

chr = ord(input("Enter any one character :")) #b   #ord function is used to convert into ascii code
if chr>=65 and chr<=90:
    print("upper case")
    elif chr>97 and chr<122:
        print("lower case")
        elif chr >48 and chr<=57:
            print("digit")
            else:
                print("special symbol")



#membership operator is used to check if the value is present or not and it include 2 operator 'in' and 'non in'
name = "help4code"
print('z' not in name )

#identity operator( for address comparison ) include same operator as membership
math = 50 
chem = 50
print(math is chem)

#for loop (initialization; condition; inc/dec)
for i in range(5): #i=0
print(i)

for i in range(2,10): #i=2
print(i)

for i in range(2,11,2): #i=5
print(i)

for i in range(5,0,-1): #i=5
print(i)

for i in range(1,11): #i=2
print(i*2)
    


for i in range(1,5):#i=1
        if i==3:
          break
        print(i)

        for i in range(1,5):#i=1
         if i==3:
          continue
        print(i)
