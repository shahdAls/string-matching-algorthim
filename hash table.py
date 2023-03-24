# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 03:34:20 2023

@author: shahd
"""

import time


import mat


start_time = time.perf_counter()
pattern="01100111110"
hash_table = {}

# Create the hash table
for i, char in enumerate(pattern):
    hash_table[char] = i

# Initialize variables to keep track of the current index and the current character
i = 0
j = 0

# Loop through the rows of the DataFrame
for index, row in (mat.df).iterrows():
    # Get the string we want to search
    text = row['joined_row']
                                                                                
    # Initialize the variables for the while loop
    i = 0
    j = 0

    while i < len(text) and j < len(pattern): #search for pattern
        # If the characters match, increment the index
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            # If the characters do not match, move the index to the next character
            if j in hash_table:
                i = i - hash_table[j]
            else:
                i += 1
            j = 0

    # If the pattern is found, print the index of the first character
    if j == len(pattern):
        print("Pattern found at index:", i - j,"the row is",index)
        
end_time = time.perf_counter()

print("Time taken:", end_time - start_time)