Task 5: Interview Questions

1. What is Pandas used for?
Pandas is the most popular Python library for data manipulation and analysis. It provides powerful data structures (like DataFrames) to handle structured data (like Excel sheets or SQL tables) efficiently.

2. What's a DataFrame?
A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet, a SQL table, or a dictionary of Series objects. It is the primary object in Pandas.

3. How do you read a CSV file?
You use the pd.read_csv() function.
import pandas as pd
df = pd.read_csv('filename.csv')

4. What is groupby()?
groupby() is a method used to split the data into groups based on some criteria (like "Category"). You can then apply a function (like sum, mean, or count) to each group independently.
# Groups by 'Category' and sums the 'Sales' for each category
df.groupby('Category')['Sales'].sum()

5. How do you filter rows?
You can filter rows using boolean indexing.
# Filters rows where 'Age' is greater than 25
filtered_df = df[df['Age'] > 25]

6. Difference between loc[] and iloc[]?
 * loc[]: Label-based selection. You use the names of the rows (index) and columns.
 * iloc[]: Integer-based selection. You use the numerical position (index) of the rows and columns (e.g., row 0, column 1).

7. What does .head() do?
.head(n) returns the first n rows of the DataFrame. By default, if you don't provide a number, it returns the first 5 rows. It's useful for quickly inspecting your data.

8. How can you create a bar chart?
You can use the .plot() method directly on a DataFrame or Series.
df.plot(kind='bar', x='Category', y='Sales')

Alternatively, you can use libraries like matplotlib or seaborn.
9. What's the shape of a DataFrame?
The .shape attribute returns a tuple representing the dimensionality of the DataFrame in the format (rows, columns). For example, (100, 5) means 100 rows and 5 columns.

10. What is NaN?
NaN stands for Not a Number. It is a special floating-point value used in Pandas (and NumPy) to represent missing or undefined data (null values).
