# Dynamic programming implementation of LCS problem 
  
# Returns length of LCS for X[0..m-1], Y[0..n-1]  
def lcs(S1, S2, len_S1, len_S2): 
    L = [[0 for x in range(len_S2+1)] for x in range(len_S1+1)] 
  
    # Following steps build L[m+1][n+1] in bottom up fashion. Note 
    # that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]  
    for i in range(len_S1+1): 
        for j in range(len_S2+1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif S1[i-1] == S2[j-1]: 
                L[i][j] = L[i-1][j-1] + 1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
  
    # Following code is used to print LCS 
    cursor = L[len_S1][len_S2] 
  
    # Create a character array to store the lcs string 
    lcs = [""] * (cursor+1) 
    lcs[cursor] = "" 
  
    # Start from the right-most-bottom-most corner and 
    # one by one store characters in lcs[] 
    i = len_S1 
    j = len_S2 
    while i > 0 and j > 0: 
  
        # If current character in X[] and Y are same, then 
        # current character is part of LCS 
        if S1[i-1] == S2[j-1]: 
            lcs[cursor-1] = S1[i-1] 
            i-=1; j-=1; cursor-=1
  
        # If not same, then find the larger of two and 
        # go in the direction of larger value 
        elif L[i-1][j] > L[i][j-1]: 
            i-=1
        else: 
            j-=1
  
    print ("Longest Common Subsequence of " + S1 + " and " + S2 + " is " + "".join(lcs))
    print ("Length of the Longest Common Subsequence is " + str(L[len_S1][len_S2]))
  
if __name__ == "__main__":
    string1 = input("Please enter a string of your choice : ")
    string2 = input("Please enter another string to compare : ")
    S1 = string1.upper()
    S2 = string2.upper()
    len_S1 = len(S1) 
    len_S2 = len(S2) 
    lcs(S1, S2, len_S1, len_S2) 