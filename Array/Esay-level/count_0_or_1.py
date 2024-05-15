
# print count of 0 and 1 in array 

def countZeroOne(arr):
    zeroCount = 0
    oneCount  = 0
    for i in range(len(arr)):
        if (arr[i]==0):
            zeroCount+=1
        else:
            oneCount+=1
    print("number of zerocount : ", zeroCount)
    print("number of onecount: ", oneCount)
arr = [1,0,1,0,0,1,1,0,1,0,1]
countZeroOne(arr)