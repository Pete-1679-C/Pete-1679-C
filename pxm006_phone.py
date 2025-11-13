# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 05:59:36 2023

@author: Pete Challenger
"""

print('Enter 10 Single Digits with the First Digit not Being 0:')
phone_number = int(input())
phone_number = str(phone_number)

print(f'\n({phone_number[0]}{phone_number[1]}{phone_number[2]}) '\
      f'{phone_number[3]}{phone_number[4]}{phone_number[5]}-'\
      f'{phone_number[6]}{phone_number[7]}{phone_number[8]}{phone_number[9]}')