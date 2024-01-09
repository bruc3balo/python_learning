import classes
# from classes import Dog

from pck.utils import print_package, random_int

bosco = classes.Dog()
bosco.talk()

print_package()

r = random_int(10)
print(f"r is {r}")