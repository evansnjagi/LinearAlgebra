# Pridict House Prices

There are many way to predict house prices, and one of them is using *Row Echelon Method (REM)*. As a learning phase, we are going to implement row reduction system that predict house prices. 


## Objectives

1. Get the data
2. Convert the data into an augmented matrix
3. Find the relationship between variable $x$ and $y$.
4. Find whether the data is unique, redundant or dependent

## Explanation

Using a real world model, we are going to predict a value, based on two featuers. 

Example system:

$$
    2x + y = 5 \\
    4x + 2y = 10
$$

Represent an augmented matrix:

$$
\left[
    \begin{array}{cc|c}
        2 & 1 & 5\\
        4 & 2 & 10
    \end{array}
\right]
$$

Solution:

$$2x + y  = 5$$

The reduced matrix will be:

$$
\left[
    \begin{array}{cc|c}
        2 & 1 & 5\\
        0 & 0 & 0
    \end{array}
\right]
$$

The last row has all trailing zeros. This means that the system data are independent.

There are *infinitely* many solution associated with the above system. 

Something else to note is that, the vectors could be *redundant*.

## Structure

```bash
row_echelon_method
├── README.md
├── data
├── main.py
├── src
└── tests

4 directories, 2 files
```

## Get the data
