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

Sample data frame

```python
from src.get_data import Getdata

# Get the dataframe
df = Getdata().get_dataframe()
```

Sample output:

```r
DataFrame shape:  (1460, 81)

Info: 
<class 'pandas.DataFrame'>
RangeIndex: 1460 entries, 0 to 1459
Data columns (total 81 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Id             1460 non-null   int64  
 1   MSSubClass     1460 non-null   int64  
 2   MSZoning       1460 non-null   str    
 3   LotFrontage    1201 non-null   float64
 4   LotArea        1460 non-null   int64  
 5   Street         1460 non-null   str    
 6   Alley          91 non-null     str    
 7   LotShape       1460 non-null   str    
 8   LandContour    1460 non-null   str    
 9   Utilities      1460 non-null   str    
 10  LotConfig      1460 non-null   str    
 11  LandSlope      1460 non-null   str    
 12  Neighborhood   1460 non-null   str    
 13  Condition1     1460 non-null   str    
 14  Condition2     1460 non-null   str    
 15  BldgType       1460 non-null   str    
 16  HouseStyle     1460 non-null   str    
 17  OverallQual    1460 non-null   int64  
 18  OverallCond    1460 non-null   int64  
 19  YearBuilt      1460 non-null   int64  
 20  YearRemodAdd   1460 non-null   int64  
 21  RoofStyle      1460 non-null   str    
 22  RoofMatl       1460 non-null   str    
 23  Exterior1st    1460 non-null   str    
 24  Exterior2nd    1460 non-null   str    
 25  MasVnrType     588 non-null    str    
 26  MasVnrArea     1452 non-null   float64
 27  ExterQual      1460 non-null   str    
 28  ExterCond      1460 non-null   str    
 29  Foundation     1460 non-null   str    
 30  BsmtQual       1423 non-null   str    
 31  BsmtCond       1423 non-null   str    
 32  BsmtExposure   1422 non-null   str    
 33  BsmtFinType1   1423 non-null   str    
 34  BsmtFinSF1     1460 non-null   int64  
 35  BsmtFinType2   1422 non-null   str    
 36  BsmtFinSF2     1460 non-null   int64  
 37  BsmtUnfSF      1460 non-null   int64  
 38  TotalBsmtSF    1460 non-null   int64  
 39  Heating        1460 non-null   str    
 40  HeatingQC      1460 non-null   str    
 41  CentralAir     1460 non-null   str    
 42  Electrical     1459 non-null   str    
 43  1stFlrSF       1460 non-null   int64  
 44  2ndFlrSF       1460 non-null   int64  
 45  LowQualFinSF   1460 non-null   int64  
 46  GrLivArea      1460 non-null   int64  
 47  BsmtFullBath   1460 non-null   int64  
 48  BsmtHalfBath   1460 non-null   int64  
 49  FullBath       1460 non-null   int64  
 50  HalfBath       1460 non-null   int64  
 51  BedroomAbvGr   1460 non-null   int64  
 52  KitchenAbvGr   1460 non-null   int64  
 53  KitchenQual    1460 non-null   str    
 54  TotRmsAbvGrd   1460 non-null   int64  
 55  Functional     1460 non-null   str    
 56  Fireplaces     1460 non-null   int64  
 57  FireplaceQu    770 non-null    str    
 58  GarageType     1379 non-null   str    
 59  GarageYrBlt    1379 non-null   float64
 60  GarageFinish   1379 non-null   str    
 61  GarageCars     1460 non-null   int64  
 62  GarageArea     1460 non-null   int64  
 63  GarageQual     1379 non-null   str    
 64  GarageCond     1379 non-null   str    
 65  PavedDrive     1460 non-null   str    
 66  WoodDeckSF     1460 non-null   int64  
 67  OpenPorchSF    1460 non-null   int64  
 68  EnclosedPorch  1460 non-null   int64  
 69  3SsnPorch      1460 non-null   int64  
 70  ScreenPorch    1460 non-null   int64  
 71  PoolArea       1460 non-null   int64  
 72  PoolQC         7 non-null      str    
 73  Fence          281 non-null    str    
 74  MiscFeature    54 non-null     str    
 75  MiscVal        1460 non-null   int64  
 76  MoSold         1460 non-null   int64  
 77  YrSold         1460 non-null   int64  
 78  SaleType       1460 non-null   str    
 79  SaleCondition  1460 non-null   str    
 80  SalePrice      1460 non-null   int64  
dtypes: float64(3), int64(35), str(43)
memory usage: 924.0 KB
None

 Top 5 houses: 
   Id  MSSubClass MSZoning  LotFrontage  LotArea Street  ... MiscVal MoSold YrSold SaleType SaleCondition SalePrice
0   1          60       RL         65.0     8450   Pave  ...       0      2   2008       WD        Normal    208500
1   2          20       RL         80.0     9600   Pave  ...       0      5   2007       WD        Normal    181500
2   3          60       RL         68.0    11250   Pave  ...       0      9   2008       WD        Normal    223500
3   4          70       RL         60.0     9550   Pave  ...       0      2   2006       WD       Abnorml    140000
4   5          60       RL         84.0    14260   Pave  ...       0     12   2008       WD        Normal    250000

[5 rows x 81 columns]
```

This is what we will use:

- **Target vector** - SalePrice
- **Feature matrix** - [LotFrontage, LotArea]

Users can choose any features of their choice.

To get the augmented matrix, run the code below:

```python
from src.get_data import Getdata

# Get augmented matrix
aug_matri = Getdata().get_augmented_matrix(feature1, feature2, target_vector)
```
You can keep the default as it but it is posible to change:

1. The root directory where the data is located as: 
```python
rp = Getdata(root_path = <"Your_root_path_of_choice">)
```
2. By default, the target vector is the `SalePrice`. You can change that.


To get a complete summary of the dataframe and the augmented matrix run the command below:

```bash
python -m tests.get_data_test
```


