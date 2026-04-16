# Mall customer segmentation using Linear Algebra concepts.
---

## Overview

Using linear algebra concepts, this project analyzes mall customer data to help businesses identify similar customers and make informed data-driven decisions.

### Objectives
- Understand customer patterns.
- Measure similarity between customers.
- Identify customer groups.

## Structure

Example of the structure used:

```bash
mall-customer-segmantation
├── README.md
├── data/
├── images/
├── notebooks/
├── requirements.txt
├── src/
└── tests/

6 directories, 2 files
```

## Dataset

The data set used in this project is from from kaggle, and it's about mall customer dataset. It has 200 rows and 7 columns. 

### Extract the data

The data is downloaded as a zip file. 

Extract it using the following command

```bash
unzip archived.zip
```

The result output will be a `'Mall Customers.xlsx'` file. 

### Loading the data

The dataset is loaded using pandas, and important features selected. These features are: Age, Income, and Spending score. 

The selected features are converted into a 3D matrix as follows:

$$x_i = (Age, Income, Spending)$$

This implies that the matrix $X \in \mathbb{R}^{200 \times 3}$.

Example of how to get the data:

The code snippet

```python

from src.load_data import load_dataset

```

In the bash, run the following command to test it out.

```bash
python -m tests.load_data.test
```
You will get a selected numerical features in a matrix format. 


## Similarity analysis

Similarity analysis is computed to know how similar customers are. This is done in linear algebra using eucledean distance formula $d(x, y) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2 + (x_3 - y_3)^3}$.

Running the test, you will get the results as follows:

```r
Customer 1 Vs. Customer 2 Distance: 41.70
Customer 1 Vs. Customer 3 Distance: 106.88
Customer 1 Vs. Customer 4 Distance: 64.57
Customer 1 Vs. Customer 5 Distance: 68.34
Customer 2 Vs. Customer 3 Distance: 85.77
Customer 2 Vs. Customer 4 Distance: 46.86
Customer 2 Vs. Customer 5 Distance: 40.14
Customer 3 Vs. Customer 4 Distance: 67.42
Customer 3 Vs. Customer 5 Distance: 70.73
Customer 4 Vs. Customer 5 Distance: 48.59
```

## Customer recommender

Using cosine similarity with the formula below: 
$$cos(\theta) = \frac{\textbf{A}\cdot \textbf{B}}{||\textbf{A}|| ||\textbf{B}||}$$

We have a defined `find_similar_customer()` that will help us to get the indices of most similar customers based on the similarity cosine matrix.

The function takes in three parameters: The matrix $X\in \mathbb{R}^{200 \times 3}$, reference customer index, and the number of others customers to do the comparison with. 

Example:
```python
indices = find_similar_customers(X, 2, 5)
```
The main function then converts the indices to their original dataframe. 

Example output:

```bash
    CustomerID Gender  Age   Education  Marital Status  Annual Income (k$)  Spending Score (1-100)
7            8      F   23  High School        Unknown                  18                      94
3            4      F   23  High School        Unknown                  16                      77
5            6      F   22     Graduate        Married                  17                      76
15          16      M   22      Unknown        Unknown                  20                      79
13          14      F   24     Graduate        Unknown                  20                      77
```

## Requirements

This project requires use of dependancies like:
- numpy
- pandas
- matplotlib
- scikit-learn

These dependancies are included in the `requirements.txt` file. 

Installing modules example:
```bash
pip install -r requirements.txt
```

## How to run the project

### Step 0. Clone repository

```bash 
git clone <your-repo-url>
cd mall_customer_segmentation
```

The following are different phases of running the project, step by step.
### Step 1: Loading the data

Inside the test folder, run `load_data_test.py` file as follows:

```bash
python -m tests.load_data_test
```

### Step 2. Compute similarity test.

```bash
python -m tests.similarity_test
```
### Step3. Customer recommendation.

To get the indices of similary customers based on similarity cosine, run the following command

```bash
python -m tests.customer_recommendatations_test
```

### Final step. Get similary customers

The final step is to get a dataframe of segmented customers. They are sorted with the highest similar customers coming first.

To get the dataframe run the following bash command:

```bash
python -m main
```

## Architecture

- Data Layer → load_data.py
- Feature Matrix → X ∈ R^{200×3}
- Similarity Engine → cosine similarity
- Output Layer → ranked customers
