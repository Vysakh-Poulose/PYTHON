lenlow=int(input())
lenhigh=int(input())
widlow=int(input())
widhigh=int(input())


ans=1
for i in range(lenlow,lenhigh+1):
  for j in range(widlow,widhigh+1):
    a=0
    while(1):
      if(i>j):
        i=i-j
      elif(j>i):
        j=j-i
      else:
        a=a+1
        break
      a=a+1
    ans=ans+a
    
print(ans)