'''BRUTE FORCE:
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
=>take an temp array with all elements equal to zeros  and a loop and add elements from the array to temp which is not equal to 0
TIME COMPLEXITY:O(N)
SPACE COMPLEXITY:O(N)
but we cannot do this approach in given they said no additional space taken
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
CODE:
----
class Solution(object):
    def moveZeroes(self, nums):
        temp=[0 for i in range(len(nums))]
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
               temp[j]=nums[i]
               j+=1 
        return temp 
  ===========================================================================================================================================================================
  optimized approach :
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  => just observe the array and question they said the non zeros elemnst should be the same sequence so we can add elemnts at last by swapping
  => by using two pointer approach we can do take an i position where the position of zero element and j=i+1
  =>and check each element from array at  j position if lement at j position is not zero and swap element at i to pos j 
  time complexity:O(N)
  space complexity:O(1)
  code:
  ----------------''''
  class Solution(object):
    def moveZeroes(self, nums):
        i=0
        while i<len(nums):
            if nums[i]==0:
                break 
            else:
                i+=1 
        k=i
        j=i+1
        while k<len(nums) and j<len(nums):
            if nums[j]!=0:
                nums[k]=nums[j]
                nums[j]=0
                k+=1
            j+=1 
'''  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  question:
  -----------------------------------------------------------------------------------------------------------------------------------------------------------
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
---------------------------------------------------------------------------------------------------------------------------------------'''
