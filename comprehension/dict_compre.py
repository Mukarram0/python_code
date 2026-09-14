chai={
    "ginger tea":100,
    "cold coffee":200,
    "green tea":150,
}

beverages={key:value/100 for key,value in chai.items() }
print(beverages)