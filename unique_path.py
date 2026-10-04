'''
🚶 Unique Paths — 2D DP

Let's learn this from zero, just like we did with Climbing Stairs. No code initially.

1. Proper Infosys-style question

You are given a grid with M rows and N columns.

A robot starts at the top-left cell (0, 0) and wants to reach the bottom-right cell (M-1, N-1).

The robot can move only:

Right →
Down ↓

The robot cannot move left or up.

Find the total number of different paths the robot can take to reach the destination.

2. How will you recognize this in the exam? ⭐⭐⭐⭐⭐

Look for these words:

grid
matrix
rows and columns
top-left
bottom-right
start
destination
move right
move down
number of ways
number of paths

When you see:

GRID / MATRIX
       +
RIGHT / DOWN
       +
NUMBER OF WAYS / PATHS

Test case-
Input:
3 3

Output:
6
'''

import sys

def solve():

    data=sys.stdin.read().split()

    if not data:
        return

    m=int(data[0])
    n=int(data[1])

    if n==0 or m==0:
        print(0)
        return

    dp=[[0]*n for _ in range(m)]

    for i in range(m):
        dp[i][0]=1

    for j in range(n):
        dp[0][j]=1

    for i in range(1 , m):
        for j in range(1 , n):
            dp[i][j]=dp[i-1][j] + dp[i][j-1]

    print(dp[m-1][n-1])

if __name__=="__main__":
    solve()


