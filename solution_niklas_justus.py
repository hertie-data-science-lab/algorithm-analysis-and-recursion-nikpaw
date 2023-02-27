# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 18:39:25 2023

@author: niklas und justus
"""

def hanoi_tower(n, first, final, extra):
    if n == 1:
        print(f"Move disk 1 from {first} to {final}")
        return
    hanoi_tower(n-1, first, extra, final)
    print(f"Move disk {n} from {first} to {final}")
    hanoi_tower(n-1, extra, final, first)

# Driver code
n = 3
hanoi_tower(n, 'Start', 'Target', 'Extra')
