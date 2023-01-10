import re
def rem_vowel(str):
    return(re.sub("[aeiouAEIOU]","",str))
str=input("enter the string")
print(rem_vowel(str))
