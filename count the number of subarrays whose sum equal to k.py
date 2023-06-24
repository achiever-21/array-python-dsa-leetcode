'''brute force:
=> by using two for loops we can solve this but the time complexity will be O(n*2)
=>first loop iterates from start to end of array 
=>second loop is for making subarrays of an array
=============================================*CODE*==================================================================================================================='''
c=0
for i in range(len(nums)):
  sum1=0
  for j in range(i,len(nums)):
    sum1+=nums[j] 
    if sum1==k:
      c+=1 
return c 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
optimized approach:
---------------
=> by using hashing we can solve this first take an dic and check if sum-k present in d 
=> if it is there increment the value of c by key value of d
=========================================****CODE***======================================================================================================================'''
d={0:1}
ans=0
sum1=0
for i in nums:
  sum1+=i 
  if sum1-k in d:
    ans+=d[sum1-k] 
  if sum1 not in d:
    d[sum1]=1
  else:
    d[sum1]+=1 
    
