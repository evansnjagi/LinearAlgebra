# Linear Transformation Engine

Implementing matrix multiplication(operations) using core linear algebra concepts

## Overview

This project implements core linear algebra concepts without using Python, without relying on external libraries like `numpy`.

The goal is to understand linear algebra operations, get a clear intuition of the core ideas behind matrix-vector multiplication, and understand it's operation in data science. 

Implement matrix and vector multiplication from scratch

Finally, understand linear transformation.

## Project structure

This is the structure adopted for this project

```bash
linear_transformation_engine
├── README.md
├── main.py
├── src
└── tests
```

## Concepts covered

1. Matrix
2. vectors
3. Dot product
4. Matrix-vector multiplication
5. Linear transformation

## Implementation

Inside the `src` folder, we have a `mat_vec.py` file. We are going to write the source code there.

Suppose we have a matrix

 $$
 \textbf{A} =
     \begin{\bmatrix}
        2 & 1\\
        0 & 3
    \end{\bmatrix}
 $$

 and a vector

 $$
    \textbf(x) = 
    \begin{\bmatrix}
        4\\5
    \end{\bmatrix}
 $$

 We want to have a transformation 

 $$
    \begin{\cases}
        y_1 = 2x_1 + x_2\\
        y_2 = 3x_2
    \end{\cases}
 $$

 resulting to a solution of $y_1 = 4$ and $y_2 = 15$.

 To test the code, run the command below.

 ```bash
 python -m tests.mat_vect_test
 ```

 Expected output:

 ``