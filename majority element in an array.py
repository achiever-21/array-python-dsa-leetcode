"""QUESTION:
169. Majority Element
Easy
15.3K
455
Companies
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
brute force:
=>take an dict and store all elemnt with count
=> after find the eleemnt where count>n/2 
=>return
=>but time complexity for storing eleemnts in a dict is O(logn)+O(n)
=>again for searching O(n)
time complexity:O(nlogn)
space complexity:O(n)
===========================================************CODE***************================================================================================================'''
d={}
for i in range(n):
  if i not in d:
    d[i]=1
  else:
  d[i]+=1 
for i ,k in d.items():
  if k>n/2:
  return d[i]
  ========================================================================================================================================================================
  optimized:
  => tale an temp and store first index 
  => after run a loop check it with other number if it is equal increment count by 1 else -1
  =>if c==0 change the temp ele with another ele
  =>and repet the same 
  tiem complexity:O(n)
  space complexity:O(1)
  -------------------------------------------*code*-------------------------------------------------------------------------------------------------------------------------------
  k=arr[0]
  c=0
  for i in range(1,len(arr)):
    if c==0:
      k=arr[i] 
    if arr[i]==k:
    c+=1 
    else:
    c-=1 
  return k
  
