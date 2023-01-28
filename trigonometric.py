'''Python program to get the value of of theta in degree and use it to find sine,cosine and tangent'''
import math as m
degree=int(input("Enter value of theta in degree\t"))
degree=m.radians(degree)
sine=(m.sin(degree))
cosine=(m.cos(degree))
tangent=(m.tan(degree))
print(f"The value of sine is {sine}")
print(f"The value of cosine is{cosine}")
print(f"The value of tangent is {tangent}")
