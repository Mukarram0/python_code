#The primary benefits are reducing code duplication, improving readability by keeping variables tightly scoped to where they are used, and avoiding redundant function calls.
while(user_input:=input("enter a value or exit: ").lower())!="exit":
    print("You entered:", user_input)