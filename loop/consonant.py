def find_consonant(c,count):
    cont=''
    for i in c:
        if(i!='a' and i!='e' and i!='i' and i!='o' and i!='u'):
            cont=i
            break
    for i in c:
        if(cont==i):
            count+=1
    print("The consonant is:",cont)
    print("The count of consonant is:",count)


con="Afrozf".lower()
find_consonant(con,0)
