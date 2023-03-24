# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 20:55:29 2023

@author: shahd
"""
import mat
import time
import pandas as pd

start_time = time.perf_counter()

# Convert the elements of a specific column to strings
# Define the pattern we want to search for
pattern = "10100110101"
def naive_string_matching(text, pattern):
    n = len(text)
    m = len(pattern)
    i = 0
    j = 0
    stack = []
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            stack.append(i - j)
            i += 1
            j = 0
        if j == m:
            return i - j
    return -1
# Loop through the rows of the DataFrame

result=-1
for row, st in enumerate((mat.df)["joined_row"]):
    # Compare the current string to the target string
    col=naive_string_matching(st,pattern)
    if col!=-1:
     # If a match is found, store the index in the result variable
      result =row
      break
 # Print the result
if result != -1:
     print("Match found at index", result," at col",col)
else:
     print("No match found.")
     
     
end_time = time.perf_counter()
print("Time taken:", end_time - start_time)

