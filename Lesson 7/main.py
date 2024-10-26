from pyexpat.errors import messages

age=25
age_as_str=str(age)
print(age_as_str, "type of",type(age_as_str))

x=32
y=5.3
result = x+y
print(type(result))

message = "i am "+str(age)+" years old"
print(message)

#this will generate an error
#z=int("abc")

name = input("enter your name")
print(f"hello,{name}")

nr1=input("Enter youre first number: ")
nr2=input("Enter youre second number ")

rezultati=int(nr1+nr2)
print(rezultati)


try:
    result=10/0
except ZeroDivisionError:
    print("nuk bon me pjestu me 0")


try:
    text="Fjalia eshte "
    text_to_int=int(text)
except Exception as e:
    print("An error occurred while parsing the data")
else:
    print("division successfully done")
finally:#this is activated always with or without errors
    print("this is always running")

