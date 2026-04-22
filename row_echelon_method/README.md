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
├── data/
├── main.py
├── src/
└── tests/

4 directories, 2 files
```

## Get the data

The house price data is in the `data/` folder, and it's called: `house-prices-advanced-regression-techniques.zip`. 

The first thing we are going to do is rename the zip file to `data.zip` using the following command

```bash
mv data/house-prices-advanced-regression-techniques.zip data/data.zip
```

Unzip the zip file

```bash
cd data/
unzip data.zip
```

A couple of files will be visible. In this project, we are only going to work with `train.csv` so, we are going to rename it to data.csv and remove all the remaining files. 

```bash
mv train.csv data.csv
rm data.zip data_description.txt sample_submission.csv test.csv
```

Get the first five data of the `train.csv` file

```bash
head -n 5 data/data.csv
```

Results:

```r
A,Y,298,0,0,0,0,0,NA,NA,NA,0,5,2007,WD,Normal,181500
3,60,RL,68,11250,Pave,NA,IR1,Lvl,AllPub,Inside,Gtl,CollgCr,Norm,Norm,1Fam,2Story,7,5,2001,2002,Gable,CompShg,VinylSd,VinylSd,BrkFace,162,Gd,TA,PConc,Gd,TA,Mn,GLQ,486,Unf,0,434,920,GasA,Ex,Y,SBrkr,920,866,0,1786,1,0,2,1,3,1,Gd,6,Typ,1,TA,Attchd,2001,RFn,2,608,TA,TA,Y,0,42,0,0,0,0,NA,NA,NA,0,9,2008,WD,Normal,223500
4,70,RL,60,9550,Pave,NA,IR1,Lvl,AllPub,Corner,Gtl,Crawfor,Norm,Norm,1Fam,2Story,7,5,1915,1970,Gable,CompShg,WdSdng, Wd Shng,None,0,TA,TA,BrkTil,TA,Gd,No,ALQ,216,Unf,0,540,756,GasA,Gd,Y,SBrkr,961,756,0,1717,1,0,1,0,3,1,Gd,7,Typ,1,Gd,Detchd,1998,Unf,3,642,TA,TA,Y,0,35,272,0,0,0,NA,NA,NA,0,2,2006,WD,Abnorml,140000

```
It's hard to unpack what the file entails. The resultant output is realy verbose and hard to read. 

We now have a file of the dataset we are going to work on `data.csv`. Inside `src/get_data.py` file, we are going to write the script of getting the two features and a target into an augmented matrix.