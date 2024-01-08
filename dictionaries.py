#Dictionaries
customer = {
    "name" : "Bruce",
    "age" : 12,
    "is_alive" : True,
}

#Access
print(f"customer name {customer['name']}")

#Yelling
try:
    print(f"error dob {customer['dob']}")
except KeyError:
    print(f"error dob not found")
except:
    print("Something went wrong")

#safe
print(f"dob not yelling {customer.get('dob')}")

#Default 
print(f"default dob {customer.get('dob', 'March 12 1998')}")

#update dict
customer['dob'] = "1998"
print(customer['dob'])

#inset dist
customer['ethnicity'] = "Kenyan"
print(customer)