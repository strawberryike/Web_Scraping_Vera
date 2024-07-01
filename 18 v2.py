# function of each rule individually
# store and loop values of each rule
# print

import numpy as np
import matplotlib.pyplot as plt

def rule1(left, center, right):
    index = 7 - (left * 4 + center * 2 + right)
    return 1 if (index & (1 << center)) else 0
left, center, right = 1, 1, 1
index = rule1(left, center, right)
print(f"Resulting index: {index}")

# {0, 0, 0, 1, 0, 0, 1, 0}
# 111, 110, 101, 100, 011, 010, 001, 000

def rule2(left, center, right):
    index = 7 - (left * 4 + center * 2 + right)
    return 1 if (index & (1 << center)) else 0
left, center, right = 1, 1, 0
index = rule2(left, center, right)
print(f"Resulting index: {index}")

def rule3(left, center, right):
    index = 7 - (left * 4 + center * 2 + right)
    return 1 if (index & (1 << center)) else 0
left, center, right = 1, 0, 1
index = rule3(left, center, right)
print(f"Resulting index: {index}")

def rule4(left, center, right):
    index = 7 - (left * 4 + center * 2 + right)
    return 1 if (index & (1 << center)) else 0
left, center, right = 1, 0, 0
index = rule4(left, center, right)
print(f"Resulting index: {index}")

def rule5(left, center, right):
    index = 7 - (left * 4 + center * 2 + right)
    return 1 if (index & (1 << center)) else 0
left, center, right = 0, 1, 1
index = rule5(left, center, right)
print(f"Resulting index: {index}")

def rule6(left, center, right):
    index = 7 - (left * 4 + center * 2 + right)
    return 1 if (index & (1 << center)) else 0
left, center, right = 0, 1, 0
index = rule6(left, center, right)
print(f"Resulting index: {index}")

def rule7(left, center, right):
    index = 7 - (left * 4 + center * 2 + right)
    return 1 if (index & (1 << center)) else 0
left, center, right = 0, 0, 1
index = rule7(left, center, right)
print(f"Resulting index: {index}")

def rule8(left, center, right):
    index = 7 - (left * 4 + center * 2 + right)
    return 1 if (index & (1 << center)) else 0
left, center, right = 0, 0, 0
index = rule8(left, center, right)
print(f"Resulting index: {index}")


