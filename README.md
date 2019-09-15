Algorithm for Longest Common Sequence program:


Step 1: Take two strings ‘string1’ and ‘string2’ as an input from the user.

Step 2: Convert both strings to upper case and store them in variables ‘S1’ and ‘S2’ respectively. This is to maintain uniformity.

Step 3: Find out the length of both strings and store them in variables ‘len_S1’ and ‘len_S2’ respectively.

Step 4: Create a function called ‘longestCommonSubsequence’ which would take ‘S1’, ‘S2’, ‘len_S1’ and ‘len_S2’ as an input to derive the longest common subsequence using the recursive method. In the code L[i][j] contains length of LCS of S1[0..i-1] and S2[0..j-1]. In case length of both strings is ‘0’ then LCS would be ‘0’. If last characters of both strings match S1[i-1] == S2[j-1] then length of LCS, L[i][j] = L[i-1][j-1] + 1. But if last characters do not match then L[i][j] = max(L[i-1][j], L[i][j-1]).

Step 5: Length of LCS is stored in L[len_S1][len_S2], now need to create a character array lcs[] of length equal to the length of lcs plus 1 (one extra to store \0) in order to store the letters in common subsequence. Traverse in bottom up fashion starting from L[len_S1][len_S2], if letters in both strings are some S1[i-1] == S2[j-1] then it’s part of LCS. Else compare values of L[i-1][j] and L[i][j-1] and go in direction of greater value.

Step 6: Print the longest common subsequence and its length as an output. 



3.	Algorithm for Pattern Match program:


Step 1: Take two inputs from the user, one as ‘string’ and the other one as 'pattern'.

Step 2: Convert both inputs to upper case and store them in variables ‘S1’ and ‘S2’ respectively. This is to maintain uniformity.

Step 3: Create a function called ‘PatternMatch’ would take ‘S1’ and ‘S2’ as an input to derive if the pattern S2 matches the string S1 using the recursive method. A matrix needs to be formed and in case both the inputs are of 0 length the output should be ‘True’ i.e. matrix[0][0] = True. 

Step 4: In case the first string is empty but there is just ‘*’ or another character followed by ‘*’ then it can be eliminated, and the result would be true. Hence the matrix value needs to be updated by one before previous value. matrix[i][0] = matrix[i - 2][0] when S2[i - 1] == '*' .

Step 5: If the characters in both inputs match or there is dot ‘.’ in S2 then the matrix value needs to be updated by the diagonal element, matrix[j][i] = matrix[j - 1][i - 1].

Step 6: If there is ‘*’ character in S2 then depending on the character at same position in S1 it will either eliminate the previous or count the previous hence the matrix would either refer to the one before previous or the previous therefore, matrix[j][i] = matrix[j - 2][i] or matrix[j - 1][i]. 

Step 7: If S2’s previous character is equal to the current S1 character with helps of ‘*’, then status can be propagated from the left, matrix[j][i] |= matrix[j][i - 1].

Step 8: The final result is stored in matrix[-1][-1] and will be displayed as ‘TRUE’ or “FALSE’.

