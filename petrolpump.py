d=[]
def knapsack(b,d,w,n):
 if(b[n-1]>w):
  return knapsack(b,d,w,n-1)
 else:
  return max(d[n-1]+knapsack(b,d,w-b[n-1],n-1),knapsack(b,d,w,n-1))
arr=input('Enter the array')
a=arr.split()
new_arr=[]
sum=0
#a=[int(x) for x in input().split()]
for i in a:
            sum=sum+int(i)
            new_arr.append(int(i))
val=new_arr.copy()
weight=sum/2
print (knapsack(new_arr,val,weight,i))
def DIFF(lst1,lst2):
  li_dif = [i for i in lst1 + lst2 if i not in lst1 or i not in lst2]
  return li_dif
res= DIFF(d,val)
for i in range(0, len(res)): 
    ans= ans+res[i]
print(ans)