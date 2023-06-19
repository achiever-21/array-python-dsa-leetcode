'''brute force:
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
=> first divide array into subarrays by using two for loops 
=> and check sum of subarray equal to k 
=>if it equal note the max len 
=> and check it for all
time complexity:O(n*2)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
for i in range(n):
  for j in range(i,n):
    sum+=arr[i] 
  if sum ==k:
    max1=max(max1,j-i+1)
return max1 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''optimized by using hashing:
******************************************************************************HASHING*******************************************************************************
=> take hash dictionary 
=>take a loop and add each element 
=> after check each condition if sum==k 
=> note the maxlen of subrayy which we added 
=>and store it in dic vth index 
=> further adding check sum-k is present in dic 
=> if it is then note length compare it with prevous max length
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
#code:
d={}
sum=0
max1=0
for i in range(n):
  sum+=arr[i]
  if sum==k:
    max1=max(max1,i+1)
  if sum-k in d:
    max1=max(max1,i-d[sum-k])
   if sum not in d:
    d[sum]=i 
print(max1)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

