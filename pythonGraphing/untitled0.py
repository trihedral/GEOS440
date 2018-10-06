#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:05:10 2018

@author: kyle
"""

x = 10   # int
y = 20.8 # float (decimal)
z = x*y
print (z)

s1 = "Hello there" # string   
s2 = "Buddy"

print (s1 + " " + s2)
print ("The number is, " + str(z))

print ("The type of z is, ")
print ( type(z) )



num = 1

if num > 5:
    print ("The number is greater than 5")
else:
    print ("The number is less than 5")
    
print ("Done with if")

num = 0
for i in range(1,21):
    num = num + 5
print (num)
    
while num < 200:
    num = num - 7
print (num)
