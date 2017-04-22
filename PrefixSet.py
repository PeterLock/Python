# -*- coding: utf-8 -*-
'''
Short Problem Definition:
Given a table A of N integers from 0 to N-1 calculate the smallest such index
 P, that that {A[0],…,A[N-1]} = {A[0],…,A[P]}.

Link
PrefixSet

Complexity:
expected worst-case time complexity is O(N)

expected worst-case space complexity is O(N)

Execution:
Based on the number of elements that can occur in N, you either mark the occurrences
 in a boolean array, or put them in a set. The last occurrence of an element that was
  not seen before is the result.
'''

def solution(A):
    seen = set()
    smallest_prefix_idx = 0
     
    for idx in xrange(len(A)):
        if A[idx] not in seen:
            seen.add(A[idx])
            smallest_prefix_idx = idx
             
    return smallest_prefix_idx
