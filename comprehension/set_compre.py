fruits=["apple","banana","cherry","kiwi","mango","apple","banana"]
# Using set comprehension to get unique fruits from the list
unique_fruits={fruit for fruit in fruits}
print(unique_fruits)


students={
    "key1":["John", "Doe", 20],
    "key2":["Jane", "Smith", 22],
    "key3":["Bob", "Johnson", 21]
}

std={item for value in students.values() for item in value} 
print(std)