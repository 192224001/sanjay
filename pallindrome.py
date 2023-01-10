def pallindrome(j):
    return j==j[::1]
j="malyalam"
ans=pallindrome(j)
if ans:
    print("yes")
else:
    print("no")
