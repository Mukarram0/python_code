chai_order=dict(type="Masala_chai",size="medium",sugar=1)
print(f"order:{chai_order}")

chai={}
chai['sugar']=2;
chai['leaves']=3;
chai['brand']="Tata"
print(f"spoon of sugar: {chai['sugar']}")
print(f"spoont of tea leaves:{chai['leaves']} ")
print(f"tea brand: {chai['brand']}")
del chai['brand']
print("brand is deleted.")
print(chai)