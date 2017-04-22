# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
'''
Short Problem Definition:
Find a maximal set of non((-))overlapping segments.

Complexity:
expected worst-case time complexity is O(N)

expected worst-case space complexity is O(N)

Execution:
This can be solved by using greedy search. The beginning of the next segment must come strictly 
after its predecessor.

'''

def solution(A, B):
    if len(A) < 1:
        return 0
     
    cnt = 1
    prev_end = B[0]
     
    for idx in xrange(1, len(A)):
        if A[idx] > prev_end:
            cnt += 1
            prev_end = B[idx]
     
    return cnt
