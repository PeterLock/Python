# -*- coding: utf-8 -*-
def solution(X, Y, D):
    
    print("Here we are")
    if Y < X or D <= 0:
        raise Exception("Invalid arguments")
         
    if (Y- X) % D == 0:
        return (Y- X) // D
    else:
        return ((Y- X) // D) + 1
    
    