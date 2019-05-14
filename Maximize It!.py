from itertools import product
first=list(map(int,input().split()))
k=first[0]
m=first[1]
list2=[]
list1=[]
total=0
for x in range(k):
    val=list(map(int,input().split()))
    list2.append(val[1:])
    total+=val[0]
result=map(lambda x:sum(i**2 for i in x)%m,product(*list2))
print(max(result))


