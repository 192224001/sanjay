def maxarea(a,len):
    area=0
    for i in range(len):
        for j in range(i+1,len):
            area=max(area,min(a[j],a[i])*(j-i))
    return area
a=[1,3,5,3]
b=[3,1,2,4,5]
len1=len(a)
print (maxarea(a,len1))
len2=len(b)
print(maxarea(b,len2))
