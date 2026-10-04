# 2D Dynamic Programming

This repository contains my practice problems based on **2D Dynamic Programming (DP)** using Python.

The problems in this folder focus on understanding DP with **grids/matrices**, where a solution is built by using previously calculated states from neighboring cells.

---

## 🧠 What I am Practicing

Through these problems, I am practicing:

* Understanding 2D DP
* Working with grids and matrices
* Identifying DP states
* Building a DP table
* Moving through a grid using Right and Down
* Counting the number of paths
* Finding the minimum path cost
* Using previously calculated cells to solve the current cell

---

## 📚 Problems

| # | Problem          | Pattern        |
| - | ---------------- | -------------- |
| 1 | Unique Paths     | Number of Ways |
| 2 | Minimum Path Sum | Minimum Cost   |

---

## 1. Unique Paths

### Problem

You are given a grid with `M` rows and `N` columns.

A robot starts at the **top-left cell `(0,0)`** and wants to reach the **bottom-right cell `(M-1,N-1)`**.

The robot can move only:

* Right →
* Down ↓

Find the total number of different paths the robot can take to reach the destination.

### Example

```text
Input:
3 3

Output:
6
```

### How to Recognize It

Look for:

```text
GRID / MATRIX
      +
RIGHT / DOWN
      +
NUMBER OF WAYS / PATHS
```

Then think:

```text
        2D DP
          ↓
    Number of Paths
          ↓
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

The current cell gets the number of ways from:

* The cell above
* The cell to the left

---

## 2. Minimum Path Sum

### Problem

You are given a grid of `M` rows and `N` columns. Each cell contains a non-negative integer representing the cost of entering that cell.

Start from the **top-left cell `(0,0)`** and reach the **bottom-right cell `(M-1,N-1)`**.

You can move only:

* Right →
* Down ↓

Find the minimum possible sum of the costs along the path.

### Example

```text
Input:
3 3

1 3 1
1 5 1
4 2 1

Output:
7
```

### How to Recognize It

Look for:

```text
GRID / MATRIX
      +
START → DESTINATION
      +
RIGHT / DOWN
      +
MINIMUM COST / MINIMUM SUM
```

Then think:

```text
        2D DP
          ↓
     Minimum Cost
          ↓
dp[i][j] = current + minimum(above, left)
```

The current cell is reached from either:

* The cell above
* The cell to the left

The smaller previous cost is selected.

---

# 🔎 2D DP Pattern Recognition

The two problems in this folder use a similar **grid-based DP structure**, but the question asks for a different result.

### Unique Paths

```text
GRID
  +
RIGHT / DOWN
  +
NUMBER OF WAYS
      ↓
   2D DP
      ↓
above + left
```

### Minimum Path Sum

```text
GRID
  +
RIGHT / DOWN
  +
MINIMUM COST
      ↓
   2D DP
      ↓
current + minimum(above, left)
```

### Key Difference

```text
Unique Paths
     ↓
Count paths


Minimum Path Sum
     ↓
Find minimum cost
```

---

# 🎯 Key Learning

The main idea I am practicing in this folder is:

> **Use the results of neighboring cells to calculate the result for the current cell.**

A 2D DP table allows the solution to store the result for each position in the grid and reuse those results for the next positions.

---

# 💻 Language

**Python**

The solutions use Python and `sys.stdin` for coding-exam-style input handling.

---

## 🚀 Goal

Continue practicing different **2D Dynamic Programming patterns** and improve my ability to recognize whether a grid problem requires **counting paths, finding minimum cost, or another DP-based approach**.
