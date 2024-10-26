class Rectangle:
    def __init__(self,gjatesia, gjeresia): #konstruktori i klases
        #parametrat para klases
        self.length = gjatesia
        self.width = gjeresia
    def calculate_area(self):
        return self.length * self.width
    def calculate_perimeter(self):
        return 2*(self.length + self.width)

katrori= Rectangle(2,5)

syprina = katrori.calculate_area()
print(syprina)

perimetri = katrori.calculate_perimeter()
print(perimetri)

