
# print all extrem elment in the array   optimal approch solution 

'''
    arr = [10,20,30,40,50,60]
output  = 10 60 20 50 30 40
'''
# Time complexity => O(n)
def printExtreme(arr):
    first = 0
    last = len(arr)-1
    while(first <= last):
        if first==last:
            print(arr[first],end=" ")
        else:
            print(arr[first],end=" ")
            print(arr[last],end=" ")
        first+=1
        last-=1






arr = [10,20,30,40,50,60,70]
printExtreme(arr)   