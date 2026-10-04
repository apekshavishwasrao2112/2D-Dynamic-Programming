'''
🟦 Minimum Path Sum — 2D DP
You are given a grid of M rows and N columns. Each cell contains a non-negative integer representing the cost of entering that cell.
Start from the top-left cell (0,0) and reach the bottom-right cell (M-1,N-1).
You can move only:

Right →
Down ↓

Find the minimum possible sum of the costs along the path.

This is a good next step because it uses **almost the same grid idea** you just learned.

### How to recognize it

When you see:

```text
GRID / MATRIX
+
START → DESTINATION
+
MOVE RIGHT / DOWN
+
MINIMUM COST / MINIMUM SUM
```

think:

> **2D DP → Minimum Path Sum**

The difference from Unique Paths is:

```text
Unique Paths
→ NUMBER OF WAYS
→ dp[i][j] = above + left

Minimum Path Sum
→ MINIMUM COST
→ dp[i][j] = current + minimum(above, left)
```
Test Case-

Input:
3 3
1 3 1
1 5 1
4 2 1

Output:
7
'''

import sys

def solve():

    data=sys.stdin.read().split()

    if not data:
        return

    m=int(data[0])#row
    n=int(data[1])#column

    if m==0 or n==0:
        print(0)
        return

    cost=[[0]*n for _ in range(m)]

    index=2

    for i in range(m):
        for j in range(n):
            cost[i][j]=int(data[index])
            index+=1
    '''
    cost=
    1 3 1
    1 5 1
    4 2 1
    '''        

    dp=[[0]*n for _ in range(m)]

    dp[0][0]=cost[0][0]
    '''
    dp=
    1 0 0
    0 0 0
    0 0 0
    '''

    for i in range(1, m):
        dp[i][0]=cost[i][0] + dp[i-1][0]

    for j in range(1, n):
        dp[0][j]=cost[0][j] + dp[0][j-1]
    '''
    dp=
    1 4 5
    2 0 0
    6 0 0
    '''

    for i in range(1 , m):
        for j in range(1 , n):
            if dp[i-1][j] < dp[i][j-1]:
                dp[i][j]=cost[i][j]+dp[i-1][j]
            else:
                dp[i][j]=cost[i][j]+dp[i][j-1]

    print(dp[m-1][n-1])

if __name__=="__main__":
    solve()

