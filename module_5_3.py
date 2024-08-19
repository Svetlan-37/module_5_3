class House:
    def __init__(self, name, number_of_floors, value):
        self.name = name
        self.number_of_floors = number_of_floors
        self.value = value

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, value):       
        return self.number_of_floors + self.value

    def __radd__(self, value):
        return self.value + self.number_of_floors

    def __iadd__(self, value):
        self.value += int
        return self

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors


h1 = House('ЖК Эльбрус', 10, 10)
h2 = House('ЖК Акация', 20, 10)

print(h1)
print(h2)
print(h1 == h2)   # __eq__
h1.number_of_floors = h1 + int    # __add__
print(h1)
print(h1 == h2)
h2.number_of_floors = int + h2    # __radd__
print(h2)
h1.number_of_floors = h1 + int    # __iadd__
print(h2)
print(h1 < h2)    # __lt__
print(h1 <= h2)   # __le__
print(h1 > h2)    # __gt__
print(h1 >= h2)   # __ge__
print(h1 != h2)   # __ne__