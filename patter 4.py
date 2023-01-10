n=int(input("enter the number of rows"))
for i in range(2,n*2):
    k=0.0
    for j in range(2,i):
        k=k+0.1
        print('%0.1f'%k,end="")
    print()
