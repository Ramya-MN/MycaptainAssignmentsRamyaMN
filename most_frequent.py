def most_frequent(str):
    d={}
    for i in set1:
        count=0
        for j in str:
            if i==j:
                count+=1
        d[i]=count
    return d

str=input("Enter a string:")
set1=set(str)
d1=most_frequent(str)
sort_d=sorted(d1.items(), key= lambda x:x[1] , reverse=True)
for i in sort_d:
    print(i[0],"=",i[1])