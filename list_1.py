list1 = [3, 5, 9, 11]

list2 = [num**2 for num in list1 if num > 9]
print(list2)

fruits = ['apple', 'orange', 'banana']

# Using a list comprehension to create a new list with each word repeated twice
doubled_fruits = [fruit for fruit in fruits]

print(doubled_fruits)
