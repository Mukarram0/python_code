animals=[
    "wild cat",
    "wild dog",
    "horse",
    "pet rabbit",
    "bison",
    "pet dog",
    "pet cat",
]
# comprehension means creating a new list from an existing list using a single line of code. It is a concise way to create lists based on existing lists.
# syntax: [expression for item in iterable if condition == True]
# make entire list in the memory
wild_animal=[animal for animal in animals if "wild" in animal]
print(wild_animal)
