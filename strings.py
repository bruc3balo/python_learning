#
course = "Python for me"
multilineStrnig = '''

    I love cake
    
    yeey
'''
print(multilineStrnig)

# Print first char of string
print(course[0])
print(course[-1])

#Print from end of string
print(course[-2])

#Print range from 0 : -3
print(course[0:-3])

#Print range from 0 : end
# can be used to copy strings
print(course[:])

###Formatting
first = input('Enter your first name ')
last = input('Enter your last name ')
message = first + ' ' + last + ' is a coder'

#Format a string
msg = f'{first} {last} is a python coder'
print(message.upper())
print(msg.lower())

# -1 == not found
print(msg.find('Balo'))

#replace
print(msg.replace("Bruce", "thwwick3rman"))

#Exists
print("Balo exists " + str('Balo' in msg))

#First letter upper rest lower
print('this'.title())

#Length of string
print(len('three'))
