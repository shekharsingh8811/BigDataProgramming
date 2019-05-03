class Regex(object):
    def PatternMatch(self, S1, S2):
        # The DP table and the string s and p use the same indexes i and j, but
        # table[i][j] means the match status between p[:i] and s[:j], i.e.
        # table[0][0] means the match status of two empty strings, and
        # table[1][1] means the match status of p[0] and s[0]. Therefore, when
        # refering to the i-th and the j-th characters of p and s for updating
        # table[i][j], we use p[i - 1] and s[j - 1].

        # Initialize the table with False. The first row is satisfied.
        matrix = [[False] * (len(S1) + 1) for _ in range(len(S2) + 1)]

        # Update the corner case of matching two empty strings.
        matrix[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        for i in range(2, len(S2) + 1):
            matrix[i][0] = matrix[i - 2][0] and S2[i - 1] == '*'

        for i in range(1, len(S1) + 1):
            for j in range(1, len(S2) + 1):
                if S2[j - 1] != "*":
                    # Update the table by referring the diagonal element.
                    matrix[j][i] = matrix[j - 1][i - 1] and \
                                (S2[j - 1] == S1[i - 1] or S2[j - 1] == '.')
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    matrix[j][i] = matrix[j - 2][i] or matrix[j - 1][i]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    if S2[j - 2] == S1[i - 1] or S2[j - 2] == '.':
                        matrix[j][i] |= matrix[j][i - 1]

        if matrix[-1][-1] == True:
            print ("TRUE, the string: " + S1 + " does match the pattern: " + S2)
        else: 
            print ("FALSE, the string: " + S1 + " does not match the pattern: " + S2)


if __name__ == "__main__":
    match = Regex
    string = input("Please enter a string of your choice : ")
    pattern = input("Please enter the pattern to compare : ")
    S1 = string.upper()
    S2 = pattern.upper()
    match().PatternMatch(S1, S2)