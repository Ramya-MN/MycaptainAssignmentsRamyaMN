list1=[]
n=int(input("Enter how many numbers do you want to enter:"))
print("Enter any {} intergers".format(n))
for i in range(n):
    j=int(input())
    list1.append(j)
print(list1)
print("The positive numbers from the given list is")
for i in list1:
    if i>0:
        print(i,end=" ")
