# Mall customer segmentation using Linear Algbra concepts.
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

Similarity analysis is computed to know how similar customers are. This is done in linear algebra using eucledean distance formula $\frac{d2 -d1}{\sqrt{x^2 + y^2 + z^2}}$.

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
