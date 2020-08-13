def prange(u):
 prlst=[2]
 for val in range(0,u+1): 
    if val > 1: 
        for n in range(2, val//2 + 2): 
            if (val % n) == 0: 
                break
            else: 
                if n==val//2 + 1:  
                    prlst.append(val)
 return prlst  
que=input().strip().split()
d=int(que[0])
p=int(que[1])
pr=prange(d)
c=0
print(pr)
#rlst=[x for x in range(1,d+1)]
#print(rlst)
ran=int(d/p)
print (ran)
lst=[]
for j in range(p):
    k=(ran*j)
    r=ran*(j+1)
    rlst=[x for x in range(k+1,r+1)]
    for i in range(k,r):
        if(i in pr):
           lst.append(rlst.index(i))
c=dict((x,lst.count(x)) for x in set(lst))
cn=0
print(c)

