
# find the missing number in the array 

# find sum of natural number 
def sumofNatural(n):
    sum1 = 0
    for i in range(1,n+1):
        sum1+=i
    return sum1
    # print(sum1)

def missingNumber(arr):
    n = len(arr)
    # print(n)
    natural = sumofNatural(n)
    # print(natural)
    sum2 = 0
    for i in range(n):
        sum2+=arr[i]
    # print(sum2)
    return natural - sum2

arr = [0,1,2,3,4,6,7]
missing = missingNumber(arr)
print("missing number in the array :",missing)
