# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 22:13:32 2024

@author: ACER
"""

while True:
    a = float(input("Nhap vao so tu [-89.9; 88.8]: "))
    if -89.9 <= a <= 88.8:
        break
    else:
        print("Khong hop le")