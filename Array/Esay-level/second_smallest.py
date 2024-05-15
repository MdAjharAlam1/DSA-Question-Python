
# print second smallest element and smallest number in the array 

def smallestNumber(arr):
    min_number = arr[0]
    for i in range(len(arr)):
        if(arr[i]<min_number):
            min_number = arr[i]
    return min_number
def secondSmallest(arr,smallest):
    second_min = 99999
    for i in range(len(arr)):
        if(arr[i]<second_min and arr[i]!=smallest):
            second_min = arr[i]
    return second_min

arr = [0,1,2,3,5,6,7,9]
smallest = smallestNumber(arr)
print("smallest number in the array : ", smallest)

second_smallest = secondSmallest(arr,smallest)
print("Second smallest number in the array :" , second_smallest)