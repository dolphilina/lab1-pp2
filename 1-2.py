class Myclass:
    x = 5
p1 = Myclass()
print(p1.x)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#comment
        """
        a bigger one 
        c
        o
        m
        m
        e
        n
        t
        """
        
x = 5
print(type(x))
#int
x = "not a comment"
print(type(x))
x = 20.5
#string
print(type(x))
#float
x = ["apple", "banana", "cherry"]
print(type(x))
#list
x = ("apple", "banana", "cherry")
print(type(x))
# tuple
x = {"name" : "John", "age" : 36}
print(type(x))
# dict
x = True
print(type(x))
# bool