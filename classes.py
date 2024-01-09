#pascal case
class Point:
    def move(self):
        print('move')
    
    def draw(self):
        print('draw')
        

point1 = Point()

#Can add attributes on the fly, woooww
point1.x = 10
point1.draw()

print(point1.x)


class Point2:
    
    #Init is the constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
  
    
    def to_string(self):
        print(f"x : {self.x} , y: {self.y}")        

point2 = Point2(10, 20)
point2.x = 15
point2.to_string()



### inheritance

#pass means pass this line e.g.
# 2 line breaks after class and function def
class EmptyClass:
    pass

class Mammal:
    def talk(self):
        print('...')
        
        
class Dog(Mammal):
    def talk(self):
        return super().talk()


class Human(Mammal):
    
    #Override method
    def talk(self):
        print("Hi")


bob = Human()
bob.talk()


def module_class():
    pass