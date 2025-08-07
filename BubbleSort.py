mylist = [70,12,4,10,3,1,15,2,9,66]
def BubbleSort(arr):
   
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
           if arr[j]> arr[j+1]:
              arr[j], arr[j+1] = arr[j+1],arr[j]


    print(arr)


BubbleSort(mylist)
