def search_element(element,arr,count):
    for i in range(0,len(arr)):
        if (element==arr[i]):
            print(f"{i} position: element={arr[i]}")
            count=count+1
    return count
            


arr=[10,20,30,40,30,20]
count=search_element(100,arr,0)
if(count==0):
    print("-1")


