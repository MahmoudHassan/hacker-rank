"""
Context
Given a 6*6 2D Array, A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:

a b c
  d
e f g
There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

Input Format

There are 6 lines of input, where each line contains 6 space-separated integers describing 2D Array ;
 A every value in A will be in the inclusive range of  -9 to 9.


Constraints
-9=< A[i][j] <=9
0=< i,j <=5

Output Format

Print the largest (maximum) hourglass sum found in A.

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output

19

"""

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    arr = []
    hourglass = []
    hourglass_list = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for row in range(4):
        for col in range(4):
            hourglass = [x[col:col+3] for x in arr[row:row+3]]
            hourglass[1][0:3:2] = [0, 0]
            hourglass_list.append(sum([sum(l) for l in hourglass]))
    print(max(hourglass_list))
