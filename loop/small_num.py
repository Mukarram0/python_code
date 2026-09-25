def smallest(arr,small,S_small):
    for i in arr:
        if(i<small):
            s_small=small
            small=i
        elif(i<S_small and i!=small):
            S_small=i
    print(f"smallest={small} and Second smallest={S_small}")

arr=[10,-2,3,22,4,5,-2,0]
smallest(arr,float('inf'),float('inf'))