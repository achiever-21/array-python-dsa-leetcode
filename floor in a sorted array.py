'''
brute force approach :
-----------------------
1.Floor is the largets ele which is less than or equal to our given k
=>linearly traverse the array stop if arr[i]==k then return i
=>if arr[i]>k stop their and return i-1 
=>Time complexity :O(n)
=>space compelxity:O(1)
==============================================================**************CODE*************==============================================================================='''
for i in range(len(nums)):
  if i==k:
    return k
  elif i>k:
    return i-1 
============================================================================================================================================================================
'''
optimal approach:
=>BY using binarysearch we can do this 
=>take two pointers low=0 and high=length(arr)-1 
=>same as binary search but if mid of arr equls to k break and return index
=>if mid of arr greater than k then decease high =mid-1 
=>if mid of arr less than k then ans=index(mid) and increment low=mid+1 
================================*CODE*====================================================================================================================================='''
low=0
high=n-1
while low<=high:
  mid=(low+high)//2
  if arr[mid]==k:
    ans=mid
    break 
  elif arr[mid]<k:
    ans=mid 
    low=mid+1
  else:
    ans=mid 
    high=mid-1 
return ans
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
