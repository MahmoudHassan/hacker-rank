"""
Consider the following version of Bubble Sort:

for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;

    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }

    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
}


Task
Given  an array, n, of size n distinct elements, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following 3 lines:

1-Array is sorted in numSwaps swaps.
    where numSwaps is the number of swaps that took place.
2-First Element: firstElement
    where firstElement is the first element in the sorted array.
3-Last Element: lastElement
    where lastElement is the last element in the sorted array.
Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.

Input Format

The first line contains an integer, n, denoting the number of elements in array a.
The second line contains n space-separated integers describing the respective values of a[0],a[1],a[2]...a[n-1].

Output Format

Print the following three lines of output:

Array is sorted in numSwaps swaps.
where  is the number of swaps that took place.
First Element: firstElement
where  is the first element in the sorted array.
Last Element: lastElement
where  is the last element in the sorted array.
Output Format

Print the following three lines of output:

Array is sorted in numSwaps swaps.
where numSwaps is the number of swaps that took place.
First Element: firstElement
where firstElement is the first element in the sorted array.
Last Element: lastElement
where lastElement is the last element in the sorted array.

Sample Input 0

3
1 2 3
Sample Output 0

Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
"""
# !/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numberOfSwaps = 0


def swap(pos1, pos2):
    a[pos1], a[pos2] = a[pos2], a[pos1]


for i in range(0, n):
    for j in range(0, n - 1):
        if a[j] > a[j + 1]:
            swap(j, j + 1)
            numberOfSwaps += 1
print("Array is sorted in {} swaps.".format(numberOfSwaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))
