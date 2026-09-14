fruits=["apple","banana","cherry","kiwi","mango"]

# Using generator expression to create a generator object
# save memory as it generates items on the fly one by one instead of storing all items in memory at once
fruit_generator=(fruit for fruit in fruits)
print(fruit_generator,"\n")  # Output: <generator object <genexpr> at 0x7f8c8c8c8c8c>

# in generator we can use inbuilt function
num=[1,2,3,4,5]

total=sum(n for n in num)
print(total)  # Output: 15