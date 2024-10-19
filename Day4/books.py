books ={
    ('1984','George Orwell'):'Dytopian',
    ('To kill moking bird', 'Harper Lee'):'Classic',
    ('The great gatby','F.Scott Fitzgerald'):'Classic'
}
#defined a dictionary with a tuple set of title and author as key and genres as values

books[("prilli i thyer" , "Ismail Kadare")] = "Novel" #add a new item to the dictionary
books_info = books[("The great gatby",'F.Scott Fitzgerald')]
print(books_info) #Print out the value of this key above

books[("Harry Potter" , "J.K. Rowling")] = "Novel" #Here is a added tuple with two elements that is a dictionary key ,that also has its value
print(books) #prints dictionary with later added


#mbledhni numrat nga 1 deri 50
#1)
def mblidhNumrat():
    return sum(range(1,101))
rezultati = mblidhNumrat()
print(rezultati)

#2)
shuma=0
for y in range (1,101):
    shuma = shuma +y
print(shuma)