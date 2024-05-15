
# print unique number in the array by XOR operator 

'''
XOR operator 
a   b   ouput 
0   0      0
0   1      1
1   0      1
1   1      0
'''

def findUnique(arr,n):
    ans = 0
    for i in range(n):
        ans = ans^arr[i]
    return ans


arr = [1,2,3,4,1,2,3,5,5]
n = len(arr)
output = findUnique(arr,n)
print(output)

