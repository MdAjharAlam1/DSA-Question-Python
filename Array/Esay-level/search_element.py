
# given target number search in array if target is found print found and not found by linear search

def linearSerach(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            # found
            return True
    else:
        # not found
        return False
    
arr = [1,2,4,6,7,10,15]
target = 12
ans = linearSerach(arr,target)
if ans==True:
    print("Found")
else:
    print("not found")