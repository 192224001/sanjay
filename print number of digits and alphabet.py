alpha,string=0,"malar5698"
for i in string:
    if(i.isalpha()):
        alpha+=1
print("number of digits is",len(string)-alpha)
print("number of alphabets is",alpha)
