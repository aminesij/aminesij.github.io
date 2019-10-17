# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:16:55 2019

@author: Amine
"""

#Fahrenheit

def f_to_c(temp_f):
    c = (temp_f - 32) * (5 / 9)
    print(c)
    
def c_to_f(temp_c):
    f = (temp_c * (9 / 5)) + 32
    print(f)
    
    



def temp_conv(scale1, scale2, temp):
    if scale1 == F & scale2 == C:
        print(f_to_c(temp))
    elif scale1 == C & scale2 == F:
        print(c_to_f(temp))
    else: print("error")
        
    
    
    
temp_conv(F, C, 70)

          