
# print even number in the array and also count it 

arr = [1,3,4,5,6,7,8,10]

count = 0

for i in range(len(arr)):
    if arr[i]%2==0:
        count+=1
        print(arr[i])
print("count of even number:", count)