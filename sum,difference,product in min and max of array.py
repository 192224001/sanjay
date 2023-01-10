def getmin(arr,n):
    result=arr[0]
    for i in range(1,n):
        result=min(result,arr[i])
        return result
def getmax(arr,n):
    result=arr[0]
    for i in range(1,n):
        result=max(result,arr[i])
        return result
def findsum(arr,n):
    min = getmin(arr,n)
    max = getmax(arr,n)
    return min+max
def finddifferent(arr,n):
    min = getmin(arr,n)
    max = getmax(arr,n)
    return min-max
def findproduct(arr,n):
     min = getmin(arr,n)
     max = getmax(arr,n)
     return min*max
if __name__ == "__main__":
    arr=[12,56,89,95,1,12]
    n=len(arr)
    print("the maximum number is ",max(arr))
    print("the minimum number is",min(arr))
    print("sum=",findsum(arr,n))
    print("different=",finddifferent(arr,n))
    print("produt=",findproduct(arr,n))
   
   
    
