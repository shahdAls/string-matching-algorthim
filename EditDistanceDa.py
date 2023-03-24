# -*- coding: utf-8 -*-\
    

#Edit Distance Algorthim by using Dataframe
import pandas as pd 
import time

start_time = time.perf_counter()

# Create a dataframe to store the data
df = pd.DataFrame(columns=['Pattern'])
df = pd.read_csv("pcr_data.csv")
df = df.astype(str)
# Join all the elements in each row with no separator
df["joined_row"] = df.apply(lambda row: ''.join(row), axis=1)
  
# Function to find the minimum of three numbers 
def minimum(a, b, c): 
    return min(min(a, b), c) 
  
# Function to calculate the edit distance between two strings 
def editDistDP(str1, str2): 
    # Create a data frame with size (len(str1)+1)*(len(str2)+1)  
    df = pd.DataFrame(columns = range(len(str2) + 1), index = range(len(str1) + 1)) 

    # Fill the first row and column with 0's  
    for i in range(len(df.columns)): 
        df.iloc[0][i] = i 

    for j in range (len(df.index)): 
        df.iloc[j][0] = j

    # Fill the data frame with edit distance values  
    for i in range (1, len (df.index)): 
        for j in range (1, len (df.columns)): 

            if str1[i-1] == str2[j-1]: 
                cost = 0

            else: 
                cost = 1

            df.iloc[i][j] = minimum((df.iloc[i-1][j] + 1), (df.iloc[i][j-1] + 1), (df.iloc[i-1][j-1] + cost))

    return df


end_time = time.perf_counter()
pattren = "01001111110"
for i in df["joined_row"]:
    print("The distance between row ", i, "=",editDistDP(pattren, i))
    

print("Time taken:", end_time - start_time)