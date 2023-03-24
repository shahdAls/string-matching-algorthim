# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 14:35:45 2023
@author: shahd
"""

import pandas as pd

import time



# Read the CSV file into a DataFrame
df = pd.read_csv("pcr_data.csv")
df = df.astype(str)
# Join all the elements in each row with no separator
df["joined_row"] = df.apply(lambda row: ''.join(row), axis=1)

# Define the target string
target = "10100110101"
# Initialize a variable to store the result
result = -1
start_time = time.perf_counter()

def naive_string_matching(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i
    return -1

# Iterate through the joined_row column of the DataFrame
for row, st in enumerate(df["joined_row"]):
    # Compare the current string to the target string
    col=naive_string_matching(st,target)
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




    
 