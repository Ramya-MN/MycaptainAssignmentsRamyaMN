list1=[]
n=int(input("Enter how many numbers do you want to enter:"))
print("Enter any {} intergers".format(n))
for i in range(n):
    j=int(input())
    list1.append(j)
print(list1)
print("The positive numbers from the given list is")
list2=[]
for i in list1:
    if i>0:
        list2.append(i)
        print(i,end=" ")
print()
print("In the list form:",list2)