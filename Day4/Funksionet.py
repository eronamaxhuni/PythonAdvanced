from pyexpat.errors import messages


def pershendetje(name="Z/Znj"):
    print("miredita si jeni",name)

#for x in range(1,100):
#   pershendetje()
pershendetje("Erona")

def shto(nr1,nr2):
    return nr1+nr2
shuma = shto(10 ,15)
print(shuma)


def greet(name):
    global message
    message = f"hello,{name}!"
    print(message)
greet("Erona")
print(message)

pershendetje()