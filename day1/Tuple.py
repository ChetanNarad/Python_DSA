# mytuple = ("chetan","Ansh","Aryan","Ayush",23,33,3.14,"Rudra")
# print(mytuple)
# print(type(mytuple))

# mytuple[2]="sunil" #immutable
# print(mytuple)

# init-tuple = ()
# print (init_tuple._len_())



# init_tuple_a = 'a', 'b'
# init_tuple_b = ('a', 'b')
# print


# init_tuple_a = '1', '2'
# init_tuple_b = ('3', '4')
# print(init_tuple_a + init_tuple_b)

# l = [1,2,3]
# init_tuple = ('Python',) * (l._len_() - l[::-1][0])
# print(init_tuple)


# init_tuple = ('Python',) * 3
# print(type(init_tuple)) # Ans will be Tuple but if delete the comma after the python it will be string


# init_tuple = (1,) * 3
# init_tuple[0] = 2
# print(init_tuple)    # Ans will be the Typeerror Object does not exist bcz tuple cant change the value


init_tuple = ((1,2),)*7
print(len(init_tuple[3:8]))
