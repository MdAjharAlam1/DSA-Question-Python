
# prnt minimum number in the array

def findMinimum(arr):
    min_number = arr[0]
    for i in range(len(arr)):
        if(arr[i] < min_number):
            min_number = arr[i]
    print("minimum-number is : ",min_number)

arr = [1,2,3,4,5,10,17]
findMinimum(arr)
