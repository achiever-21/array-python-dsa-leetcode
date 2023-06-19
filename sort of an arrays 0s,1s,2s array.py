'''brute force :
=>given an array by using 0s ,1s 2s.
=>first we can sort the array but the time complexity fro that is O(nlogn).
=>after checking count of no of 0s 1s and 2s.
=>and arrange the array by using 0s first 1 middle and 2s last.
=> thats it done 
time complexity :O(n)+O(n)
space complexity :O(3)
-----------------------------------------------*****code**********----------------------------------------------------------------------------------------------------------'''
for i in arr:
  if i==0:
    c_o+=1 
  elif i==1:
    c_1+=1 
 for i in range(n):
  if i<=c_o:
    arr[i]=0
   elif i<=c_1 and i>=c_o:
    arr[i]=1 
   else:
    arr[i]=2
 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''optimized:
=> this is little bit tricky here we have to take three proniters low,mid,high.
=>check arr[mid]=0 then swap arr[low],arr[mid] and increment low+=1,mid+=1 
=>check arr[mid]=2 then swap arr[mid],arr[high] and decreement high-=1,mid+1 
=>else mid+=1 
------------------------------------************#CODE#**************---------------------------------------------------------------------------------------------------------'''
low=0
high=n-1
mid=0
while mid<=high:
  if arr[mid]==0:
    swap(arr[mid],arr[low])
    low+=1
   elif arr[mid]==2:
    swap(arr[high],arr[mid])
    high-=1
   else:
    mid+=1
   return arr
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
