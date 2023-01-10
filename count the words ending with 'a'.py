str=input("enter a string:")
list=str.split()
words=0
for i in list:
    if(i[-1]=='a' or i[-1]=='A'):
        words+=1
print("Number of words ending with a,A is=",words)
