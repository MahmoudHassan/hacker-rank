"""
Task
Given a string,S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 spaceseparated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Input Format

The first line contains an integer, T (the number of test cases).
Each line i of the T subsequent lines contain a String, S.

Constraints
1=< T <=10
2=< Length of S <=10000

Output Format

For each String s[j] (where 0=< j <=T-1), print s[j]'s even-indexed characters, followed by a space, followed by s[j]'s odd-indexed characters.

Sample Input

2
Hacker
Rank
Sample Output

Hce akr
Rn ak
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())): s = input(); print(*["".join(s[0::2]), "".join(s[1::2])])
