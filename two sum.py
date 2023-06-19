'''brute force:
=> given an array we have to find two indexes where we add we get element k
=>so take two loops in which first elemnt is added to all elements and checks whether the number is equal to k or not 
-----------------------------------------------------------**CODE***------------------------------------------------------------------------------------------------------'''
for i in range(n):
  for j in range(i+1,n):
    if arr[i]+arr[j]==target:
      return i,j 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''optimized code:
=> By using hashing we can solve this first we have to take dic and add all elemnets in that 
=> and run a loop for traversing each (target-ele) and check  present in dict 
=>add all elements in dic and also check target-ele present in dic 
=> return return index of both numbers
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
code:'''
d={}
for i in range(n):
  if target-a[i] in d:
    return d[target-a[i]],i 
  else:
    d[a[i]]=i
   ======================================================================================================================================================================
