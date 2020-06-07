arr=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]

"""
i=0
while(arr[i]!=1):
    i+=1
print(i)
"""
def findOne(arr, l, r):
    if(arr[l]==1):
        return l
    else:
        index=1
        r=l+1
        while(arr[r]!=1):
            l = r
            r = r + index*2
            index+=1
        return findOne(arr, l+1, r)

l=0
r=1
while(arr[r]!=1):
    l=r
    r=r*2
print(findOne(arr, l, r))
