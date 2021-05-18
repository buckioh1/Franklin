# Assignment 1 Explanation

***Please Note: I was having difficulty getting GitHub to properly display the .ipynb file. If .ipynb file does not load in GitHub, download the zip folder from the repository and open using Jupyter Notebook or Google Collaboratory.***

For this assignment, I chose to use the Teams.csv file within the BaseballDataBank folder in the Franklin DATA 612 repository.

To begin, I chose to assign the data to the computer memory by utilizing the Pandas library in Python and utilizing the `read_csv()` function.
- This can be seen in `cell 1`.

Next, we were asked to show the top rows using the `.head()` function and last rows using the `.tail()` function. I chose to display the top 10 and last 5 rows.
- The `.head()` function can be found in `cell 2`.
- The `.tail()` function can be found in `cell 3`.

Once this was completed, we were asked to print the column names which was accomplished via the `.columns` attribute.
- The result can be see in `cell 4`.

Next, the assignment asked for the type of the data set which can be seen using the `type()` function.
- The result is in `cell 5`.

Following this we were asked to identify the number of rows and columns which can be done using the  `.shape` attribute. This result will display a tuple in the format: (rows, columns).
- The result is shown in `cell 6`.

Lastly, the assignment asks for the mean of several columns using the `.groupby()` function. I chose to sort the data using the 'lgID' and 'teamID' before using the `.mean()` function.
- The result can be seen in `cell 7`.
