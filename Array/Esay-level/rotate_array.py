
# # rotate an array from one place

'''
arr = [1,2,3,4,5]
ouput = [2,3,4,5]
'''
# Time Complexity => O(N)
# space complexity => O(1)


def rotateOnePlace(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(1,n,1):
        arr[i-1] = arr[i]
    arr[n-1] = temp
    return arr

arr = [1,2,3,4,5]
ans = rotateOnePlace(arr)
print(ans) 