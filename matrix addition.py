a=[[1,2,3],
   [4,5,6],
   [8,5,2]]

b=[[8,5,2],
   [2,5,8],
   [8,5,2]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(a)):
    
    for j in range(len(a[0])):
        result[i][j]= a[i][j] + b[i][j]
        
for r in result:
            print(r)
        
