
# print all odd nnumber and count the lement 

arr = [1,4,5,6,7,8,9,10]

count = 0
for i in range(len(arr)):
    if arr[i]%2==1:
        count+=1
        print(arr[i],end=" ")
print()
print("count of all odd number : ", count)