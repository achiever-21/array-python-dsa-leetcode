===========================================================>#BY USING BIT MANIPULATION #=======================================================================================>
#
code:
#no of subsets are 2*n where n=len(array)
ab=[1,2,3]
for i in range(1<<n):
  a=[]
  for j in range(n):
    if i&(1<<j):
      a.append(ab[j])
  abc.append(a)
return abc
=============================================================================================================================================================================================
