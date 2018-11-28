#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author:
# @Date  : 2018/6/25
 
b = 8
a = 0
number = 0
while number < 3:
 
    a = int(input("lucky number:"))
 
    if a > b:
        print("小一点!")
    elif a < b:
        print("大一点!")
    else:
        print("Bingo!")
        break
 
    number += 1
 
else:
    print("次数已用完!")