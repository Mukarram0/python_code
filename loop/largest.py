def largest(li,large_num,s_large):
    for i in li:
        if(i>large_num):
            s_large=large_num
            large_num=i
        elif(i>s_large and i!=large_num):
            s_large=i
    print(f"largest number: {large_num} and Second largest number: {s_large}")

arr=[10,22,201,22,201,303,303,21,56]
l=float('-inf')
s_l=float('-inf')
largest(arr,l,s_l)