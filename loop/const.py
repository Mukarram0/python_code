def find_consonant(con,count):
    cont=""
    for i in range(len(con)):
        if(con[i]!='a' and con[i]!='e' and con[i]!='i' and con[i]!='o' and con[i]!='u'):
            cont=con[i]
            break
    for i in con:
        if(cont==i):
            count+=1
    print(f"Consonant={cont} and Count={count}")


find_consonant("afrozf",0)


