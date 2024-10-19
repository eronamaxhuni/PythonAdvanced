students = ["Alma","Stina","Blini","Klea","Fat"]

for emri in students:
    print(emri)

fjalia = "Sot eshte nje dite e bukur"
for shkronja in fjalia:
    print(shkronja)

for numri in range(1,5):
    print(numri)

#gjeni maksimumin nga lista

numrat = [3,4,6,8,1,9,12,60,45,30,13,49]
#maksimumi = max(numrat)
#print("Numri me i madh nga lista numrat eshte: ",maksimumi)

maksimumi = numrat[0]
for numri in numrat:
    if numri > maksimumi:
        maksimumi = numri
print("maksimumi eshte :" ,maksimumi)


count = 1
while count <=5 :
    print("iteritation",count)
    count += 1

numbers_list=[0,5,4,71,2,3,4,57]
target = 20

for numri in numbers_list:
    print(numri)
    if numri > target:
        print("ka gabim")
        break

for numri in numbers_list:

    if numri > target:
        print(numri)
        print("ka gabim")
        continue


while True:
    user_input = input("Enter a positive number:")
    if user_input.isnumeric():
        num=int(user_input)
        if num >0:
            break
        print("invalid input.Please try again")
    print("you entered a valide positive number ",num)

for numri in range(1,101):
    if numri % 2 == 0:
        print("Numrat cift jane:",numri)