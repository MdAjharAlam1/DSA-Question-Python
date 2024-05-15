
# print all possible pair from array   brute force solution 

'''
{10,10}  {20,10}    {30,10}     {40,10}
{10,20}  {20,20}    {30,20}     {40,20}
{10,30}  {20,30}    {30,30}     {40,30}
{10,40}  {20,40}    {30,40}     {40,40}
'''

def printAllPair(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i],arr[j])

arr =[10,20,30,40]
printAllPair(arr)