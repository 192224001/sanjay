a=[]
c=[]
n=int(input("enter number of elements"))
for i in range(1,n+1):
    b=int(input("enter the element"))
    a.append(b)
n1=int(input("enter number of elements:"))
for i in range(1,n1+1):
    d=int(input("enter the element"))
    c.append(d)
new=a+c
new.sort()
print("sorted list is:",new)
