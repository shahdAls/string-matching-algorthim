# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:28:36 2023

@author: shahd
"""
import pandas as pd
import time
import queue


# Create a dataframe to store the data
df = pd.DataFrame(columns=['Pattern'])
df = pd.read_csv("pcr_data.csv")
df = df.astype(str)
# Join all the elements in each row with no separator
df["joined_row"] = df.apply(lambda row: ''.join(row), axis=1)
start_time = time.perf_counter()

  
 
#import queue

def edit_distance(str1, str2): 
    m = len(str1) 
    n = len(str2) 

    # Create a matrix to store results of subproblems 
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 

    # Fill d[][] in bottom up manner 
    for i in range(m + 1): 
        for j in range(n + 1): 

            # If first string is empty, only option is to insert all characters of second string 
            if i == 0: 
                dp[i][j] = j     # Min. operations = j

            # If second string is empty, only option is to remove all characters of second string 
            elif j == 0: 
                dp[i][j] = i     # Min. operations = i

            # If last characters are same, ignore last char and recur for remaining string 
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1]

            # If last character are different, consider all possibilities and find minimum  
            else:  
                q = queue.Queue()   # Create a queue to store the possible operations  

                q.put((dp[i][j-1], 'insert'))   # Insert operation  
                q.put((dp[i-1][j], 'remove'))   # Remove operation  
                q.put((dp[i-1][j-1], 'replace'))   # Replace operation  

                min_val = float('inf')   # Initialize min_val as infinity (max possible value)  

                while not q.empty():   # Iterate through the queue until it's empty  

                    val, opr = q.get()     # Get the current value and operation from the queue     

                    if val < min_val:     # Check if the current value is less than min_val     
                        min_val = val     # Update min_val with current value     
  

                dp[i][j] = min_val + 1     # Update the matrix with minimum value plus one (for current operation)     

    return dp[m][n] 







end_time = time.perf_counter()
pattren = "01001111110"
l=0
for i in df["joined_row"]:
    print("The distance between row ", l, "=",edit_distance(pattren, i))
    l = l+1
    

print("Time taken:", end_time - start_time)