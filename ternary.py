order_amt=int(input("enter a amount: "))
delivery_fees=0 if order_amt>300 else 30
print(f"delivery fees is {delivery_fees}")