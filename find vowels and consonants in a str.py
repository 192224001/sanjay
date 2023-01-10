str=input("enter a sentence")
vowels=0
consonants=0
for i in str:
    if(i=='a'or i=='e'or i=='i' or i=='o' or i=='u'
       or i=='A' or i=='E' or i=='O' or i=='U'):
        vowels=vowels+1
    else:
        consonants=consonants+1
print("total number of vowels in this string=",vowels)
print("total number of consonants in this string =",consonants)
