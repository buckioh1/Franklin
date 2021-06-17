# Assignment 5

## Eric Schmidt
## DATA 612: Data Mining
## Dr. AbdelRahman

### 1. Work on your selected data set and convert a column of non-categorical type into a categorical type.
I chose to select the State_Drug_Utilization_Data_2010 dataset for this problem because of the various data types and structure. I assigned the dataset to the `df` variable `DataFrame` using the `read_csv` function in Pandas.

Once this was completed I applied the `info()` function to identify all the various types of data for each column.

I determined the `Utilization Type` and `State` columns were imported as `strings` and were eligible to convert to `category` type as instructed in the assignment.

I used the `astype()` function to assign both of the columns the data type `category`.

Once completed, I veiwed the result by using the `info()` function again.

### 2. Convert another column into a string type.
I chose to convert the `string` columns `Labeler Code` and `Product Code` into `str` data types. They were imported as `int64` values.

Using the same `astype()` function in Problem 1, I chose to convert the `Labeler Code` and `Product Code` to `str` data types.

I confirmed the result by using the `info()` function.
