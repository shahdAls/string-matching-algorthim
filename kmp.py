# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:29:55 2023

@author: shahd
"""

import time
import pandas as pd



# Read the CSV file into a DataFrame
df = pd.read_csv("pcr_data.csv")
df = df.astype(str)
# Join all the elements in each row with no separator
df["joined_row"] = df.apply(lambda row: ''.join(row), axis=1)


start_time = time.perf_counter()

def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
 
    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0]*M
    j = 0  # index for pat[]
 
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
 
    i = 0  # index for txt[]
    while (N - i) >= (M - j):
        if pat[j] == txt[i]:
            i += 1
            j += 1
 
        if j == M:
            print("Found pattern at index " + str(i-j))
            j = lps[j-1]
 
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
                
 
 
 
def computeLPSArray(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix
 
    lps[0] = 0 # lps[0] is always 0
    i = 1
 
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len-1]
 
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1


for i, s in enumerate( df["joined_row"]):
    # Compare the current string to the target string
    KMPSearch(s,"11111001110")
    
    
    
    
      
end_time = time.perf_counter()
print("Time taken:", end_time - start_time)

