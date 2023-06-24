# question
Given an unsorted array, Arr[] of size N and that contains even number of occurrences for all numbers except two numbers. 
Find the two numbers in decreasing order which has odd occurrences.

Example 1:

Input:
N = 8
Arr = {4, 2, 4, 5, 2, 3, 3, 1}
Output: {5, 1} 
Explaination: 5 and 1 have odd occurrences.

Example 2:

Input:
N = 8
Arr = {1 7 5 7 5 4 7 4}
Output: {7, 1}
Explaination: 7 and 1 have odd occurrences.
You don't need to read input or print anything. Your task is to complete the function twoOddNum() which takes the array Arr[] and its size N as input parameters and returns the
two numbers in decreasing order which have odd occurrences.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
===============================================================================================================================================================================================
# BRUTE FORCE:
=>by taking loops counting each number .
=>if a number repeated odd no of times return the ele
-----------------------------------------------------------------*************CODE**********************---------------------------------------------------------------------------------
for i in range(len(arr)):
  c=0
  a=arr[i]
  for j in range(i+1,len(arr)):
    if a==arr[j]:
      c+=1 
  if c&1==1:
    ab.append(a)
return ab
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#HASHING
=> take an dic and add each element n its count of repeating if the ele already exists increment the key value of the array 
=> if ele not in dic then insert the ele in dic
---------------------------------------------------------------------------------------**CODE**--------------------------------------------------------------------------------------------
d={}
for i in arr:
  if i in d:
    d[i]+=1 
else:
  d[i]=1 
for i,k in d.items():
  if d[i]&1==1:
    return d[i]
-------------------------------------------------------------------------------------------------------------
#optimized approach 
=>first find the xor of all elements in a array
=>next check the set index of xor 
=>now divide the array into two halfs by using set index of xor
=> the elments which are having same set index are one group 
=> and other are other grup in this way we can find the xor of two groups then we get individual ele
=> it means odd times repating number .
  -----------------------------------------------***CODE******-------------------------------------------------
for i in arr:
  xor=xor^i 
while xor:
  if xor&1:
    break 
c+=1 
for i in arr:
  if i&1<<c:
    xor1=xor^i 
else:
  xor2=xor2^i 
return xor1,xor2
---------------------------------
