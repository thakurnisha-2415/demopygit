n=int(input("enter the no.: "))
for i in range(2,n):
    if (n%i==0):
        break
if i+1==n:
    print(n, " the no. is prime no.")
else:
    print(n, " the no. is not prime")