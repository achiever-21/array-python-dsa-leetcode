brute force:
=========================
=> we can take temp array store elements 
=>swap elements from k pos to 0.
after from n-k assign elemnets from temp array to given array 
timecomplexity:O(n-k)+O(k)==O(n)
space complexity:temp array=O(k)
====================================
optimized:
====================
=>by observing we can reverse array by that we can solve 
=> first given k positions if k==n then array will be same no need of doing anything
else if k>n after doing n rotation array will be same .so we can divide if suppose len array is 7 and given postions to swap is 7 then no change
if k=14 ,n=7
k=n+n
=>in this case we can simply take mod
k=k%n 
=====================================================================================================================================================================code:
-------------
class Solution:
    def leftRotate(self, arr, k, n):
        if k>n:
            k=k%n
        arr[:k]=arr[0:k][::-1]
        arr[k:]=arr[k:][::-1]
        arr[::]=arr[::-1]
        
time complexity:O(n)+O(k)+O(n-k)
space complexity:----
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
question:
==========================================================================================================================================================================
Given an array arr[] of size N and an integer K, the task is to left rotate the array K indexes

Example 1:

Input: N = 7, K = 2
arr[] = {1, 2, 3, 4, 5, 6, 7}
Output: 3 4 5 6 7 1 2
Explanation: Rotation of the above 
array by 2 will make the output array .

Example 2:

Input: N = 6, K = 12
arr[] = {1, 2, 3, 4, 5, 6}
Output: 1 2 3 4 5 6

Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function leftRotate() that takes array arr, integer K and integer N as parameters and rotate the given array by d value.

 

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
--------------------------------------------------------------------------------------============================================================================================================================================================================================

 
