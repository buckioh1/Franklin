# Assignment 4
## Eric Schmidt
## DATA 612: Data Mining
## Dr. AbdelRahman

For this assignment I chose to use several files within the baseball databank dataset avaialble on Franklin's GitHub.

My objective for this assignment was to merge several different data sources in to one data frame and perform insightful analysis that could not be completed without concatenating, joining or merging.

The first step was to load the related data sources into their own dataframes which can be seen in `Cell 2`.

Next, I decided to view the column names for each of the data frames to understand which attributes I can join on. I identified the following relationships:
- Teams.csv --> AllstarFull.csv : `yearID` & `teamID`
- AllstarFull.csv --> Salaries.csv : `yearID` & `playerID`
- Salaries.csv --> Players.csv : `playerID`

`Cell 4` thru `Cell 6` complete the merging described above.

Next, we were to identify any missing values in our dataset and clean the data.

I used the calculation of taking the entire row count and subtracting each attirbutes `count()` to determine the number of missing values. This can be seen in `Cell 7`.

The data shows 114 missing values in the `birthState` column. After exploring the data further, it appears there is missing data for players born outside of the USA. In order to address this, I chose to insert a value into this column named `International` if the value is missing. `Cell 8` accomplishes this by using the `fillna()` function in Pandas to insert the given values for all missing values.

`Cell 9` is confirmation of the number of values in the dataset to show the `fillna()` function worked as designed.

Next, I chose to make sure all missing values were truly from outside the USA. `Cell 10` shows the `value_counts()` by `birthCountry` and confirms all states are outside the USA.

Last, I chose to plot the highest salaries by All Start players in order to see if there is a trend year over year. The plot shows indeed, the salaries are generally increasing year over year.
