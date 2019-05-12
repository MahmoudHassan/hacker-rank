"""
Task
Write a Calculator class with a single method: int power(int,int).
The power method takes two integers, n and p, as parameters and returns the integer result of n**p.
If either n or p is negative, then the method must throw an exception with the message: n and p should be non-negative.

Input Format

Input from stdin is handled for you by the locked stub code in your editor. The first line contains an integer,T , the number of test cases.
Each of the T subsequent lines describes a test case in 2 space-separated integers denoting n and p, respectively.

Output Format

Output to stdout is handled for you by the locked stub code in your editor.
 There are T lines of output, where each line contains the result of n**p as calculated by your Calculator class' power method.

 Sample Input

4
3 5
2 4
-1 -2
-1 3
Sample Output

243
16
n and p should be non-negative
n and p should be non-negative
"""


# Write your code here
class Calculator:
    def power(self, n, p):
        if n < 0 or p < 0:
            raise Exception('n and p should be non-negative')
        return n ** p


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
