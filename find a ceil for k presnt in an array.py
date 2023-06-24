bruteforce:
linearsearch
=============================================================================================================================================================================
 binaryseach approach:
c=0
while low<high:
  mid=(low+high)//2
  if arr[mid]==target:
    ans=target 
    break 
  elif arr[mid]>target:
    ans=arr[mid]
    high=mid-1 
  else:
    arr[mid]<target:
    low=mid+1 
return ans 
