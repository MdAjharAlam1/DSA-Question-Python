 
# print all triplet in the array  brute force solution

def printAllTtriplet(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(arr[i],arr[j],arr[k])

arr = [1,2,3,4,5,6]
printAllTtriplet(arr)