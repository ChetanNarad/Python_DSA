#
# mylist = [
#     "prashant", "Ashish", "komal", "ankush",
#     "Ashish", 77, "sandip", 60.52, "prashant"
# ]

# print(mylist)
# print(type(mylist))   # <class 'list'>

# print(mylist[0])      # prashant
# print(mylist[1])      # Ashish
# print(mylist[2])      # komal
# print(mylist[-1])     # prashant

# print(mylist[2:5])    # n=5, n-1=4 -> "komal", "ankush", "Ashish"
# print(mylist[:5])     # n=5, n-1=4 -> "prashant", "Ashish", "komal", "ankush", "Ashish"
# print(mylist[1:])     # n=8, n-1=8 -> Ashish, komal, ankush, Ashish, 77, sandip, 60.52, prashant
# print(mylist[1:8:2]) #1,3,5,7'''

# mylist[2]="Akshay"
# print(mylist)

# if "ankush" in mylist:
#     print("yes ankush is available")
# else:
#     print('not available')


# mylist.append('harsh')
# mylist.append('laxman')
# print(mylist)
# #append() and extend() both work like same

# To insert the item at specified position

# mylist.insert(3,"sanket")
# print(mylist)

# mylist.remove("sandip")
# print(mylist)

# newlist = mylist.copy()  #cloning
# print(newlist)

# mylist = [
#     ["prashant", "jha"],
#     ["85.56"],
#     [440022, "yyy"]
# ]

# print("example of multidimensional list: ")  #display the list based on the row and column position

# #print(mylist[row][col])

# print(mylist[0][0])
# print(mylist[0][1])

# print(mylist[1][0])

# print(mylist[2][0])
# print(mylist[2][1])


# list2 =[50,25,50,'prashant']
# #del list2 [2]
# #del list2
# print(list2)

# list2 =[50,25.50,'prashant']
# list2.clear()
# print(list2)

# name="prashant" #['p','r','a']
# print(name)
# myname=list(name) #typecasting
# print(myname)
# # we have used list constructor

#sorting example
# mylist=[44,22,77,0,9,88]
# mylist.sort()
# mylist.sort(reverse=True)
# print(mylist)


#Alising Concept means assigning one vaiable reference to the another variable

# mylist=[44,22,77,0,9,88]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))

# mylist=[44,22,77,0,9,88]
# for i in mylist: 
#     print(i)

# list1 = [0,1,4,0,2,5]
# for i in list1:
#     if i == 0:
#         list1.remove(i)
#         list1.append(i)
#         print(list1)



#Questions for exams
#find the second largest from list
# mylist = [7,3,9,2,8]
# mylist.sort()
# print(mylist[-2])


# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,20,40,50,60
# print(a)
# # The answer will be value error

# a=[1,2,3,4,5]
# print(a[3:0:-1])
# The ans will be 4,3,2


# arr = [[1,2,3,4],
#        [4,5,6,7],
#        [8,9,10,11],
#        [12,13,14,15]]
# for i in range(0,4) : #i=4 #only focsed on your rows 
#     print (arr[i].pop())

#     #the answer will be 4 7 11 15


# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1] = arr[i]
#     for i in  range(0,6):
#         print(arr[i], end = " ")


A=[1,2,3]
B=[2,3,4]
C=[3,4,5]

for i in A: 
 if i in B and i in C:
        print(i)