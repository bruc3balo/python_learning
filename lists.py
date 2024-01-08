matrix = [
    [10, 9 ,8],
    [7, 6 ,5],
    [4, 3 ,2],
]

#Add number to end of list
matrix[0].append(8.5)

#Add number to index of list i.e. pushes numbers to rearrange
matrix[0].insert(1, 11)

#Remove object(item) from list
matrix[0].remove(10)


#Clear list
matrix[0].clear()

#remove item from end of list
matrix[1].pop()

#find index of item in list
print(f"index of 6 is {matrix[1].index(6)}")

#check if list contains value
print(f"list contains 6 {6 in matrix[1]}")

#find occurences in list
print(f"occurrences of 6 in list {matrix[1].count(6)}")

#Sort list
matrix[1].sort()

nums = matrix[1].copy()

print(nums)


print("===============================================")

for row in matrix:
    for number in row:
        print(number)
        
