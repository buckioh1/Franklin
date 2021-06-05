# Assignment 3 README
## Eric Schmidt
## DATA 612: Data Mining
## Dr. AbdelRahman

### 1. Create three different meaningful charts using Seaborn package on your selected data set.
I chose to create a barplot, lineplot and boxplot as my three choices for charts. I also decided to select the stocks dataset from the Franklin repository.
I began by assigning the csv dataset to a dataframe names `stocks_df`. Once this was created I decided to explore the variables to decide what insights I would like to understand.

The first thing I noticed was the improper format for all of the data. Most of the columns were imported as objects instead of useful statistical values such as `dates` or `int` or `float`.

I knew my first question in the dataset was, "Which company has the highest valuation?", so I decided to plot the highest values companies in descending order. In order to do this I needed to reformat the 'market cap' column since the values were assigned via text. 

Under `Section 1` I removed commas, separated the numeric values from the text characters and finally multiplied those numeric values by the text character multiplier. Since most copmanies are valued in the Billion dollar range, I chose to select this as the common value. For example, a company valued in the Trillions would be in the thousands of Billions and companies valued in the Millions would be in the tenths of Billions.

Once the data was formatted correctly, I was able to plot the market cap appropriately by filtering out all companies below $500B. Once this was done I found the top 9 companies by market cap.

After this, I decided it would be helpful to see the trend of stock prices for the top two companies. I was interested to see if each price correlated with each other. I took the original dataset and filtered out only the top two companies. Once this was done I was able to plot the `price_at_close` in a time series line plot. This plot confirmed by hypothesis that both companies, which are in similar industries, largely follow the same price trend.

Lastly, from prior knowledge, I'm aware the PE Ratio is a large factor when determining which companies are "over valued" or "under valued" so I wanted to see a unique distribution of all companies with their max PE Ratio over this time period. Again, I needed to edit the dataset and account for Null values. Once this was completed I was able to plot the boxplot using Seaborn. There are quite a few outliers, so I needed to filter to companies below a PE Ratio of 150 in order to see meaningful data.  Once this was completed I found the average PE Ratio is around $20 with the interquartile range betweeen $15 and $30. This tells me investing in companies above a PE Ratio of $30 assumes more risk because they are in the territory of "overvalued" and more research would be required.

## 2. Explain when it is best to use.
It is best to use Seaborn when a data story is required. Visualization is a critical part of explaining data insights and the Seaborn library makes it very simple to create professional plots with high customization. The plots I decided to use are some of the most common used in the industry because of their effectiveness in conveying a message.

## 3. Post your work in GitHub.
Please find assignment 3 in the associated folder.

## 4. Add a README file.
Completed.
