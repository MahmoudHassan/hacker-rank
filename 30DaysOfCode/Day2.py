"""
Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Input Format

There are 3 lines of numeric input:
The first line has a double, mealCost  (the cost of the meal before tax and tip).
The second line has an integer, tipPercent (the percentage of mealCost being added as tip).
The third line has an integer, taxPercent (the percentage of mealCost being added as tax).

Output Format

Print the total meal cost, where totalCost is the rounded integer result of the entire bill ( mealCost with added tax and tip).

Sample Input

12.00
20
8
Sample Output

15
"""
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):

    tip = meal_cost*(tip_percent/100)
    tax = meal_cost*(tax_percent/100)
    totalCost = meal_cost+tip+tax
    print(round(totalCost))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
