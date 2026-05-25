mydict =    {
    101: "prashant",
    102: "ashish",
    "103": "mohini",
     "104": "trivani",
     101:"ashish",
    104:"ashish"
 }
print(mydict)


# a = mydict[102]
# print(a)

# # we will replace old value by new value
# mydict[102]="peter"
# print(mydict)

#only print key x=0,1
# for x in mydict:
#     print(x)

#only print values
# for x in mydict.values():
#     print(x)


#Printing keys and values both
# for x,y in mydict.items():
#     print(x,y)


#adding a new key: value pair
# mydict["mobile_no"]=46465738848
# print(mydict)


# mydict.pop(101)
# print(mydict)

# a = {(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])


# a = {'a':1,'b':2,'c':3}
# print(a['a','b'])   key Error


# arr = {} 
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# print(arr)
# sum = 0
# for k in arr:
#     sum += arr[k]
#     print(sum)   #Ans will be 4


# my_dict = {}
# my_dict[1] = 1
# my_dict ['1']= 2
# my_dict[1.0] = 4
# print(my_dict) 
# sum = 0
# for k in my_dict:
#     sum +=my_dict[k]
#     print(sum)

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2,)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
#     print(sum)
#     print(my_dict)
#     # Answer will be 30 {(1, 2, 4): 8, (4, 2, 1): 10, (1, 2): 12}



# box = {}
# jars = {}
# crates = {}

# box['biscuit'] = 1
# box['cake'] = 3

# jars['jam'] = 4

# crates['box'] = box
# crates['jars'] = jars

# print(len(crates[box]))
# Answer will be Type error
# A. 1
# B. 3
# C. 4
# D. Type Error


# dict = {'c': 97, 'a': 96, 'b': 98}

# for _ in sorted(dict):
#     print(dict[_])

#=========================================================================================
# rec = {"Name": "Python", "Age": "20"}

# r = rec.copy()

# print(id(r) == id(rec))
#====================================================================================

# rec = {"Name": "Python", "Age": "20", "Addr": "NJ", "Country": "USA"}

# id1 = id(rec)

# del rec

# rec = {"Name": "Python", "Age": "20", "Addr": "NJ", "Country": "USA"}

# id2 = id(rec)

# print(id1 == id2)


#==============================================================================================================================================================

#Que: Find the key with maximum and minimum value in dictionary
# sample input: {"A":50,"B":30,"C":70}
#Expected Output: "C"

# key with max value in dictionary

# mydicttt = { 'A':50,'B':30 ,'C':70}
# max = 0
# for x in mydicttt.values():
#     if x>max:
#         max=x
# print(max)

# # ======================================

# min = mydicttt['A']
# for x in mydicttt.values():
#     if x<min:
#         min=x
# print(min)


#===============================================================================================================================
#Count frequency of elements in list using a dictionary:

#==========================================================================================================================

#===========================================================Reversing the Number===============================================
# num = 123
# a =num % 10
# num = num // 10
# b = num % 10
# c = num // 10
# rev = a*100 + b*10 + c*1 
# print(rev)


#123456 = 654321

Amount = int(input("Please Enter Amount for Withdraw : "))  # 630

print("100 notes=", Amount // 100)
print("50 notes =", (Amount % 100) // 50)
print("20 notes =", ((Amount % 100) % 50) // 20)
print("10 notes =", (((Amount % 100) % 50) % 20) // 10)
print("5 notes =", ((((Amount % 100) % 50) % 20) % 10) // 5)
print("2 notes =", (((((Amount % 100) % 50) % 20) % 10) % 5) // 2)
print("1 notes =", ((((((Amount % 100) % 50) % 20) % 10) % 5) % 2) // 1)

