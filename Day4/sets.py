from enum import unique

my_set = {1,2,3}
my_set = set([4,5,6])
print(my_set)

A = {34,5,7,3,4,1,2,43,2}
B = {5,22,65,7,5,8,1,2,35}

unioni = A.union(B)
print(unioni)

prerja = A.intersection(B)
print(prerja)

diferenca = A.difference(B)
print(diferenca)

#Set operations

#add an element
A.add(100)

#remove an element
A.remove(100)

#clear all the elemnts
A.clear()

#length of set
print(len(A))

my_list = [3,4,5,3,5,2]

unique_set = set(my_list)
print(unique_set) #unique of the elements

#keyword in
colors={"red","green","blue"}
color = "red"
print(color in colors)
print(colornot in colors)
