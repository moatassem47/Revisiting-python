mylist = [5,7,9,1,8,3,0,6,2,88]
key = int(input("enter the number you want to search for: "))


def LinearSearch(arr, choice):
    for i in range(len(arr)):
        if arr[i] == choice:
            print("element is at index: " + str(i))
            return i

      
    print("not found\n")
      
print(LinearSearch(mylist, key))
