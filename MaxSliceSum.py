# -*- coding: utf-8 -*-
'''
Short Problem Definition:
Find a maximum sum of a compact subsequence of array elements.


Complexity:
expected worst-case time complexity is O(N);

expected worst-case space complexity is O(N)

Execution:
The only difference to the example given by Codility is the minimal slice length, which is 1.
'''

def solution(A):
    max_ending = max_slice = -1000000
    for a in A:
        max_ending = max(a, max_ending +a)
        max_slice = max(max_slice, max_ending)
         
    return max_slice
