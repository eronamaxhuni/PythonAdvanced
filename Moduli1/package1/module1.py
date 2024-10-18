emri ='Erona'
mbiemri = 'Maxhuni'
mosha = 20

print(emri)
print(type(emri))

print(type(mosha))

mosha = mosha +10
print(mosha)

emri_mbiemri = emri +" "+ mbiemri
print(emri_mbiemri)

my_data = ['erona','maxhuni',20,'shkolla digjitale']
mosha = my_data[2]
print(mosha)

#.append -perdoret me shtu te dhena ne fund te listes
my_data.append('prishtina')

#insert perdoret per me vendos te dhena ne liste ne pozicionin me indeks te caktuar
my_data.insert(2,"prishtina")

#remove perdoret me largu dicka duke theksuar elementin ashtu siq eshte
my_data.remove('erona')

#del perdoret me fshi te dhena nga lista por duke ia caktuar indeksin
del my_data[0]
print(my_data)