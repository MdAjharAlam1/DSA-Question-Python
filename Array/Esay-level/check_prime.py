'''
given a number check number is prime or not

1. if number is prime print prime else print not prime 
'''
def checkPrime(num):
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print("number is prime",num)
    else:
        print("not a prime",num)


n = int(input("Enter your Number :- "))
checkPrime(n)