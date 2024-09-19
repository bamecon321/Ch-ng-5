# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:15:47 2024

@author: ACER
"""

n = int(input("Nhập một số nguyên dương n: "))
giai_thua = 1
for i in range(1, n + 1 ):
    giai_thua = giai_thua * i
print("Giai thua bang: ", giai_thua)
