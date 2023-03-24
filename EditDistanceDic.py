# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:27:17 2023

@author: shahd
"""

import pandas as pd
import time

start_time = time.perf_counter()

# Create a dataframe to store the data
df = pd.DataFrame(columns=['Pattern'])
df = pd.read_csv("pcr_data.csv")
df = df.astype(str)
# Join all the elements in each row with no separator
df["joined_row"] = df.apply(lambda row: ''.join(row), axis=1)


def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = {i: {j:0 for j in range(n+1)} for i in range(m+1)}
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
    return dp[m][n]


end_time = time.perf_counter()
pattren = "01001111110"
for i in df["joined_row"]:
    print("The distance between row ", i, "=",edit_distance(pattren, i))
    

print("Time taken:", end_time - start_time)