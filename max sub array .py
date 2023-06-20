'''
Kadane's Algorithm
MediumAccuracy: 36.28%Submissions: 710K+Points: 4
Join the most popular course on DSA. Master Skills & Become Employable by enrolling today! 
Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.
Example 1:
Input:
N = 5
Arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.
Example 2:

Input:
N = 4
Arr[] = {-1,-2,-3,-4}
Output:
-1
Explanation:
Max subarray sum is -1 
of element (-1)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Brute force:
=>taking two loops and doing sub arrays sums and finding max subarray from 
=time complexity:O(n*2)
=>space complexity:O(1)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
optimial:time:O(n)
space:O(1)'''
----------------------------------------------------------------********code*****************----------------------------------------------------------------------
sum=0
max1=0
for i in range(n):
  sum+=arr[i]
  max1=max(sum,max1)
  if sum<0:
    sum=0
 return max1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
