arr = [2,15,3,1,8,4,10,6] 

def qsort(arr,start,end):
    print(arr)
    if end > start: 
        print(f"Pivot: {end} {arr[end]}")
        ptr = 0
        for i in range(0,end):
            if arr[i]<arr[end]:
                tmp = arr[i]
                arr[i] = arr[ptr]
                arr[ptr] = tmp
                ptr+=1
        tmp = arr[end]
        arr[end] = arr[ptr]
        arr[ptr] = tmp 
        qsort(arr,start,ptr-1)
        qsort(arr,ptr+1,end)

qsort(arr,0,len(arr)-1) 

print(arr)