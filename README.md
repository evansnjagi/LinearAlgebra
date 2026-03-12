# Plane classifier
---
This project implements a simple classifier based on the equation of a plane in $\mathbb{R}^3$

Each data point is represented as a vector:

$$(x, y, z)$$

Where:

- x = Age
- y = Annual income
- z = Spending habits


The classifier uses the plane equation: $ax + by + cz + b = 0$ to decide which side of the plane a point lies on.

Having $f(x, y, z) = ax + by + cz$ then if:
1. $f(x, y, z) > 0$ The point lies on the left side of the plane(i.e normal).
2. $f(x, y, z) < 0$ The point lies on the right side of the plane(i.e suspicious).


## Project structure

```
mall_customer-classifier/
|
|- data/
|   Mall_Customers.csv
|- src/
|   classifier.py
|   load_data.py
|   plane.py
|- figures
|    plots.png
|- README.md
```

## Dataset

The dataset used is **mall customers**, containing information about customer age, income and spending score.

These features are mappend into a 3-D feature space for classification.

## Data loading

The dataset is stored inside the `data/` directory.

File:

    `Mall_customers.csv`


The script `src/load_data.py` is responsible for loading and converting it into a format suitable for mathematical computation.

Each row of the dataset is converted into a 3-dimensional point:

(x, y, z)

x = Age
y = Annual income
z = Spending score (between 1 and 100)

Example transformation:

1,Male,19,15,39

Becomes the point

(19, 15, 39)

These points forms a dataset in $\mathbb{R}^3$ which we will later be classified using a plane.

## Mathematical model

The classifier is based on an equation of a 3-dimension space.

$ax + by + cz + b = 0$

Where:

1.$(a, b, c)$ is the normal vector of the plane
2.$d$ is the bias term

For each point $(x, y, z)$ the classifier computes:

    $f(x, y, z) = ax + by + cz + b$

The sign of the results determines the side of the plane and thus the class as:

1. $f(x, y, z) > 0$ \righarrow Normal customers
2. $f(x, y, z) < 0$ \righarrow Suspicious customers
3. $f(x, y, z) = 0$ \righarrow On the plane

## Classification pipeline

The classification pipeline consists of three main steps:

1. Load the data using `load_data.py`
2. Define a plane using `plane.py`
3. Classify each plane base on the sign of:
$f(x, y, z) = ax + by + cz+ d$

The pipeline is implemented on the `classifier.py`.

## Running the classifier

To run the classifier:

```bash
python3 src/classifier.py
```
The program loads the data, define a plane and classify each data point based on the equaton of a plane.

## Data visualization

The dataset can be viewed in 3-dimension space by running the visualizer:

```bash
python3 src/visualize.py
```
This generated a 3-D scatter plot for all the customers. The plot is saved in `figures` directory.


## Figures

All the plots generated in this project are saved in `figures/` directory.

Example:

`figures/customer_distribution.png`