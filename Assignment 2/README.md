# Assignment 2 Explanation

***Please Note: I was having difficulty getting GitHub to properly display the .ipynb file. If .ipynb file does not load in GitHub, download the zip folder from the repository and open using Jupyter Notebook or Google Collaboratory.***

For this assignment, I chose to continue using the Teams.csv file within the BaseballDataBank folder in the Franklin DATA 612 repository.

To begin, I chose to assign the data to the computer memory by utilizing the Pandas library in Python and utilizing the `read_csv()` function.

Next, we were asked to find the maximum date within the dataset. First, I decided to use the `.info` attribute to look at all the features of the dataset and their data type.  From there I found only 1 applicable date field and it was assigned `int64` data type instead of `datetime64[ns]`.  Once this was identified, I decided to use the `pd.to_datetime()` function to change the data type from `int64` to `datetime64[ns]`.

Once this was completed, I could then use the `.max()` function to identify the maximum date in the dataset.

Next, the assignment asked for us to subtract the dates on the column from the maximum date. This was accomplished using the subtraction operator within Python. Since the data was within a Pandas DataFrame, no loop was needed.

Following this we were asked to convert the number of days generated from the previous request into number of months. This was done using the Numpy `timedelta64()` function. This function allowed us to convert the days into months and assign this value to a Pandas Series object.

Lastly, the assignment asks us to save the dataset to a csv file which was done using the `.to_csv()` function.
