# -*- coding: utf-8 -*-

'''
Short Problem Definition:
Given a set S of n distinct integers, print the size of a maximal subset S’ of S where the 
sum of any 2 numbers in S’ are not evenly divisible by k.

Link
Non-Divisible Subset

Complexity:
time complexity is O(N)

space complexity is O(N)

Execution:
This is by all means not an easy task and is also reflected by the high failure ratio of the 
participants. For a sum of two numbers to be evenly divisible by k the following condition has 
to hold. If the remainder of N1%k == r then N2%k = k-r for N1+N2 % k == 0. Let us calculate the 
set of all numbers with a remainder of r and k-r and pick the larger set. If the remainder is 
half of k such as 2 % 4 = 2 or exactly k such as 4 % 4 = 0, just one number from each of these 
sets can be contained in S’.
'''

def solveSubset(S, k, n):
    r = [0] * k
     
    for value in S:
        r[value%k] += 1
     
    result = 0
    for a in xrange(1, (k+1)//2):
        result += max(r[a], r[k-a])
    if k % 2 == 0 and r[k//2]:
        result += 1
    if r[0]:
        result += 1
    return result
     
n, k = map(int, raw_input().split())
S = map(int, raw_input().split())
print solveSubset(S, k, n)
