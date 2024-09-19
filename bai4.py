# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 21:46:59 2024

@author: ACER
"""

while True:
    a = int(input("Nhap gia tri tu [-99,99]: "))
    if -99 <= a <= 99:
        print("Hop le", a)
        break
    else:
        print("Khong hop le")