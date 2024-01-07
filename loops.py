i = 1

while i <= 5:
    print(f"{i} : {'*' * i}")
    i += 1
    
    if i == 7:
        break
else:
    print("Loop Done")
    
    
for letter in 'Python':
    print(letter)
    
for number in [1,2,3,4,5]:
    print(number)

for number in range(10):
    print(number)
    
#Range (begining, end - exclusive, steps)
for number in range(5,10, 2):
    print(number)