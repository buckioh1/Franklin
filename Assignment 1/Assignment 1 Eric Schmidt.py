#!/usr/bin/env python
# coding: utf-8

# # Assignment 1
# ## Eric Schmidt
# ## DATA 612: Data Mining
# ## Dr. AbdelRahman

# ### 1. Load the dataset of your choice from the list provided <a href="https://github.com/frankData612/data_612">here.</a>

# I will be using the Teams.csv found in the BaseballDataBank folder located in the Franklin Data_612 Repository on GitHub.

# ### 2. Load the dataset using Jupyter notebook and explore the data by using the following:

# In[5]:


import pandas as pd

# Load the csv file to a dataframe.
df = pd.read_csv("https://raw.githubusercontent.com/buckioh1/data_612/master/baseballdatabank-master/core/Teams.csv",
                sep = ',')


# #### Show the `.head()` and `.tail()` of the dataset. Specify the number of rows to print using the `.head()` and `.tail()`.

# In[6]:


# Display the first 10 rows using the ".head()" function.
df.head(10)


# In[7]:


# Display the last 5 rows using the "tail()"" function.
df.tail(5)


# #### Print the column names.

# In[18]:


# Display the column names using the 'columns' attribute.
df.columns


# #### Print to see what is the type of your data set.

# In[19]:


# Print the type of data the data set is stored as using 'type' function.
type(df)


# #### Check number of rows and columns.

# In[20]:


# Print the number of (rows, columns) in the dataset using the 'shape' attribute.
df.shape


# #### Use `groupby()` and find the mean on your selected column(s).

# In[21]:


# Use the 'groupby' function to order the data by League ID and Team ID. Then determine the average Rank, Wins and Losses.
df.groupby(['lgID', 'teamID'])[['Rank', 'W', 'L']].mean()


# #### Add a <a href="https://github.com/buckioh1/Franklin/blob/main/Assignment%201/README.md">README file.</a> in GitHub where you explain everything you did.
