Note: This notebook should be viewed in Jupyter Notebook for best results.

# Eric Schmidt

## Assignment 6
## DATA 612: Data Mining
## Dr. AbdelRahman

### Working with strings:
For this assignment, I chose to work with the stock market data provided in the Franklin 612 Git Repository.

The first task was to import the dataset using `pd.read_csv()`. Once this was completed I chose to split the company name in the data set into it's symbol and the name. I chose to do this because the symbol is often the preferred method of searching for stock quotes and historical data.

I was able to clean this column by using the regular expression `split` to break out the string between the dash ('-').

I assigned these two new values to new columns names `Symbol_cleaned` and `Name_cleaned`.

### Use of `apply.()`:
For this problem, I chose to create one function that performed each of the requested tasks (mean, addition, mode, median and range). This function also formats the number using commas and dollar signs.

Following the creation of the function, using the `.apply()` function I was able to apply this function to all the numeric columsn in the dataframe by including an `if:` statement to make sure the data types are non-objects (strings).
