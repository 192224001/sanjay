rows=int(input("enter a no of rows:"))
for i in range(rows+1):
    for j in range(i):
        print('*',end='')
    print()
