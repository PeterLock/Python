# -*- coding: utf-8 -*-
import sys
 
def solution(A):
    #1st pass
    parts = [0] * 12
    parts[0] = A[0]
  
    for idx in xrange(1, len(A)):
        parts[idx] = A[idx] + parts[idx-1]
  
    #2nd pass
    solution = sys.maxint
    print(solution)

    for idx in xrange(0, len(parts)-1):
        solution = min(solution,abs(parts[-1] - 2 * parts[idx]));  
  
    return solution