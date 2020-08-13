que=input().strip().split()
n=int(que[0])
k=int(que[1])
lst=list(map(int,input().strip().split()))
if(k<=pow(10,5)):
     for _ in range(k):
          m=int(max(lst))
          p=lst.index(m)
          lst[p]=int(m/2)
print(sum(lst))
    