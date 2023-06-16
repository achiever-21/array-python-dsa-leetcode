intution:
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
we have to make two arrays union and in ascending order
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
brute force:
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
=>we can solve this by using  set time O(n)
=>take a temp array 
=>first step
======>add all elements from the array 1 to the temp and check each element present in loop or not 
=>second
==========> same as firststep for array2 
==> sort the array 
timecomplexity:O(n)+O(m)+O(nlogn)
space complexity:O(m+n)
==========================================================================================================================================================================
optimized approach:
=> by using two pointers i and j we know mergesort where we compare each elemnt from the both sub arrays and assaign to third array 
=>the elemnt which is not present in third array(union) for searching (we can use union[-1])it decrease time complexity by comparing with last elemnt 
=>afer elemnt which is smaller add it to union array first from both arrays by checking condition if smaller ele from both array is present in union array
time complexity:O(n+m)
space complexity:union array only using for return array 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
code:
-------------
class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        i=0
        j=0
        union=[]
        while i<n and j<m:
            if a[i]<b[j]:
                self.union_append(union,a[i])
                i+=1
            else:
                self.union_append(union,b[j])
                j+=1
        while i<n:
            self.union_append(union,a[i])
            i+=1
        while j<m:
            self.union_append(union,b[j])
            j+=1
        return union
    def union_append(self,union,i):
        if len(union)>0 and union[-1]!=i:
            union.append(i)
        elif len(union)==0:
            union.append(i)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Union of two arrays can be defined as the common and distinct elements in the two arrays.
Given two sorted arrays of size n and m respectively, find their union.


Example 1:

Input: 
n = 5, arr1[] = {1, 2, 3, 4, 5}  
m = 3, arr2 [] = {1, 2, 3}
Output: 1 2 3 4 5
Explanation: Distinct elements including 
both the arrays are: 1 2 3 4 5.
 

Example 2:

Input: 
n = 5, arr1[] = {2, 2, 3, 4, 5}  
m = 5, arr2[] = {1, 1, 2, 3, 4}
Output: 1 2 3 4 5
Explanation: Distinct elements including 
both the arrays are: 1 2 3 4 5.
 

Example 3:

Input:
n = 5, arr1[] = {1, 1, 1, 1, 1}
m = 5, arr2[] = {2, 2, 2, 2, 2}
Output: 1 2
Explanation: Distinct elements including 
both the arrays are: 1 2.
--------------------------------------------------------------------------============================================================================================
