#Fibonacci series

i=0
j=1
s=0
n=int(input("Enter terms:"))
print("Fibonacci series upto {} terms ".format(n))
for k in range(1,n+1):
    print(s,end=",")

    i=j
    j=s
    s=i+j
print("...")