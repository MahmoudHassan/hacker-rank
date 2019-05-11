"""
Task
Given a base-10 integer,n, convert it to binary (base-2).
Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

Input Format

A single integer, n.

Constraints
1=< N <=1**6

Output Format

Print a single base-10 integer denoting the maximum number of consecutive i's in the binary representation of n.

Sample Input 1

5
Sample Output 1

1
Sample Input 2

13
Sample Output 2

2
"""

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    print(len(max(str(bin(n)).replace('0b', '').split('0'))))
