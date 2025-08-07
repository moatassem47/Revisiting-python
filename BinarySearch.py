def BinarySearch(arr,key):
    low = 0
    high = (len(arr) -1)

    while low<=high:
        mid = (low + high)//2
        guess = arr[mid]

        if guess == key:
            return mid
        elif guess>key:
            high = mid -1

        else:
            low = mid +1
    return None

mylist = [1,3,5,7,9]
key = int(input("what number are you searching for? : "))

print(BinarySearch(mylist,key))