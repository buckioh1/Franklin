# Eric Schmidt

## DATA 612: Data Mining

## Dr. AbdelRahman

For this assignment I chose to work with the **State_Drug_Utilization_Data** provided in the Franklin 612 repository.

For question number 1, I explained the difference between `g` input and the original `df`. The main difference is `g` is going to be the modified DataFrame in which we're interested in summarizing the key statistics and `df` is the original assigned dataset.

To begin, I imported the dataset using the Pandas `read_csv` function and assigned the variable `df` to this DataFrame. From there, I was curious about the various data types and applied the `.info()` function to look at which columns I would be interested in studying further.

I noticed the `Total Amount Reimbursed` was a figure I wanted to explore further and decided to use this as my dimention variable. Once this was decided I had the option of using `Utilization Type`, `State`, `Labeler Code` or `Product Code` as my `.groupby()` variables. Out of all these options I decided to go with `State` as it's the most meaningful variable I can relate with. After this decision was made I wanted to determine the top 10 States for Total Amount Reimbursed. This can now be acccomplished using the `summarize_data()` function shared in class.

After defining the `summarize_data()` function, I had to make a few changes which are explained in the notebook. In general, I had to change to dictionary `key` names and the associated `values`. I changed the method from `dot notation` to `bracket notation` to account for the spaces in the column name.

Finally, I chose to change the format of the numbers to account for financial, integer and percentage formats.
