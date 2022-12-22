#!/usr/bin/python3
"""
Returns a list of lists of integers representing
the pascal's triangle of n
"""
def pascal_triangle(n):
    a = [[] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j < i:
                if j == 0:
                    a[i].append(i)
                else:
                    a[i].append(a[i - 1][j - 1])
            elif j == i:
                a[i].append(1)
    return a
