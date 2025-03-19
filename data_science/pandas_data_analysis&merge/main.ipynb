# Introduction

Today we'll dive deep into a dataset all about LEGO. From the dataset we can ask whole bunch of interesting questions about the history of the LEGO company, their product offering, and which LEGO set ultimately rules them all:

<ul type="square">
<li>What is the most enormous LEGO set ever created and how many parts did it have?</li>

<li>How did the LEGO company start out? In which year were the first LEGO sets released and how many sets did the company sell when it first launched?</li>

<li>Which LEGO theme has the most sets? Is it one of LEGO's own themes like Ninjago or a theme they licensed liked Harry Potter or Marvel Superheroes?</li>

<li>When did the LEGO company really expand its product offering? Can we spot a change in the company strategy based on how many themes and sets did it released year-on-year?</li>

<li>Did LEGO sets grow in size and complexity over time? Do older LEGO 
sets tend to have more or fewer parts than newer sets?</li>
</ul>

**Data Source**

[Rebrickable](https://rebrickable.com/downloads/) has compiled data on all the LEGO pieces in existence. I recommend you use download the .csv files provided in this lesson. 
# Import Statements
from IPython.display import Image, display
display(Image(url="https://i.imgur.com/49FNOHj.jpg"))

# Data Exploration
**Challenge**: How many different colours does the LEGO company produce? Read the colors.csv file in the data folder and find the total number of unique colours. Try using the [.nunique() method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.nunique.html?highlight=nunique#pandas.DataFrame.nunique) to accomplish this.
import pandas as pd

df = pd.read_csv("data/colors.csv")
print(df.head())

# Count unique values in 'name' column
unique_colors = df["name"].nunique()

print(f"Total unique colors: {unique_colors}")




**Challenge**: Find the number of transparent colours where <code>is_trans == 't'</code> versus the number of opaque colours where <code>is_trans == 'f'</code>. See if you can accomplish this in two different ways.
df.groupby('is_trans').count()

**Challenge**: Change this into an h3 section heading: Understanding LEGO Themes vs. LEGO Sets
Walk into a LEGO store and you will see their products organised by theme. Their themes include Star Wars, Batman, Harry Potter and many more.

**Challenge**: Display this image: https://i.imgur.com/aKcwkSx.png
A lego set is a particular box of LEGO or product. Therefore, a single theme typically has many different sets.

**Challenge**: Display this image https://i.imgur.com/whB1olq.png 
The <code>sets.csv</code> data contains a list of sets over the years and the number of parts that each of these sets contained.

**Challenge**: Read the sets.csv data and take a look at the first and last couple of rows. 
from IPython.display import Image, display
display(Image(url="https://i.imgur.com/aKcwkSx.png"))
display(Image(url="https://i.imgur.com/whB1olq.png"))

import pandas as pd

df = pd.read_csv("data/sets.csv")

print(df.head())
print(df.tail())


**Challenge**: In which year were the first LEGO sets released and what were these sets called?
first_lego = df.sort_values('year', ascending=True)
print(first_lego)
**Challenge**: How many different sets did LEGO sell in their first year? How many types of LEGO products were on offer in the year the company started?
first_year = first_lego["year"].min()
first_lego = first_lego[first_lego["year"] == first_year]

# Display the first LEGO sets
print(f"First LEGO sets were released in {first_year}.\n")
print(first_lego)
**Challenge**: Find the top 5 LEGO sets with the most number of parts. 
top_lego = first_lego.sort_values('num_parts', ascending=False)
print(top_lego.head())
**Challenge**: Use <code>.groupby()</code> and <code>.count()</code> to show the number of LEGO sets released year-on-year. How do the number of sets released in 1955 compare to the number of sets released in 2019? 
group_counts = df.groupby('year').count()
print(group_counts['set_num'].head())
print(group_counts['set_num'].tail())

**Challenge**: Show the number of LEGO releases on a line chart using Matplotlib. <br>
<br>
Note that the .csv file is from late 2020, so to plot the full calendar years, you will have to exclude some data from your chart. Can you use the slicing techniques covered in Day 21 to avoid plotting the last two years? The same syntax will work on Pandas DataFrames. 
import matplotlib.pyplot as plt

group_counts_filtered = group_counts.iloc[:-2]

plt.figure(figsize=(12, 6))
plt.plot(
    group_counts_filtered.index,
    group_counts_filtered.values,
    linestyle='-',
    color='b'
)

# Add labels and title
plt.xlabel("Year")
plt.ylabel("Number of LEGO Sets Released")
plt.title("LEGO Sets Released Over the Years (Complete Years Only)")
plt.grid(True)

# Show the plot
plt.show()

### Aggregate Data with the Python .agg() Function

Let's work out the number of different themes shipped by year. This means we have to count the number of unique theme_ids per calendar year.
import pandas as pd

# Load sets.csv instead of themes.csv
df = pd.read_csv("data/sets.csv")

# remember the diffeerence between .groupby('year').count
print("Counts Total Rows per Column:\n")
print(df.groupby('year').count())

# and here ['theme_id'] is counting each unique theme_id while ('year') can be seen as index
print("Counts Unique Themes Per Year\n")
print(df.groupby('year')['theme_id'].nunique())
# using .agg for each columns
print("Using .agg\n")
themes_by_year = df.groupby('year').agg({'theme_id': pd.Series.nunique}).rename(columns={'theme_id': 'nr_themes'})
print(themes_by_year)
**Challenge**: Plot the number of themes released by year on a line chart. Only include the full calendar years (i.e., exclude 2020 and 2021). 
import matplotlib.pyplot as plt

themes_filtered = themes_by_year.iloc[:-2]

plt.figure(figsize=(12, 6))
plt.plot(
    themes_filtered.index,
    themes_filtered.values,
    linestyle='-',
    color='b'
)

# Add labels and title
plt.xlabel("Year")
plt.ylabel("Number of themes")
plt.title("Number of themes per year")
plt.grid(True)

# Show the plot
plt.show()
### Line Charts with Two Seperate Axes

**Challenge**: Use the <code>.groupby()</code> and <code>.agg()</code> function together to figure out the average number of parts per set. How many parts did the average LEGO set released in 1954 compared to say, 2017?
# getting the average parts per set so it gives fair comparison between each year
mean_parts_num = df.groupby('year').agg({'num_parts': pd.Series.mean})
print(mean_parts_num)

print(f"YEAR 1954: {mean_parts_num.loc[1954]['num_parts']}")
print(f"YEAR 2017: {mean_parts_num.loc[2017]['num_parts']}")

### Scatter Plots in Matplotlib
**Challenge**: Has the size and complexity of LEGO sets increased over time based on the number of parts? Plot the average number of parts over time using a Matplotlib scatter plot. See if you can use the [scatter plot documentation](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.scatter.html) before I show you the solution. Do you spot a trend in the chart? 
import matplotlib.pyplot as plt

# Exclude the last two years (assuming they are incomplete)
mean_parts_num_filtered = mean_parts_num.iloc[:-2]

plt.figure(figsize=(12, 6))
plt.scatter(
    mean_parts_num_filtered.index,
    mean_parts_num_filtered.num_parts,  # Explicitly reference the column
    color='b',
    alpha=0.5  # Optional: Makes points semi-transparent
)

# Add labels and title
plt.xlabel("Year")
plt.ylabel("Mean number of parts")
plt.title("Mean Number of Parts per Year")
plt.grid(True)

# Show the plot
plt.show()

### Number of Sets per LEGO Theme
LEGO has licensed many hit franchises from Harry Potter to Marvel Super Heros to many others. But which theme has the largest number of individual sets? 
print(mean_parts_num.idxmax()[0])  # Extract the index (year) with the max value
print("----------\n")
print(mean_parts_num.loc[2020, 'num_parts'])  # Get the actual mean parts value for 2020

**Challenge** Use what you know about HTML markup and tags to display the database schema: https://i.imgur.com/Sg4lcjx.png

### Database Schemas, Foreign Keys and Merging DataFrames

The themes.csv file has the actual theme names. The sets .csv has <code>theme_ids</code> which link to the <code>id</code> column in the themes.csv. 
**Challenge**: Explore the themes.csv. How is it structured? Search for the name 'Star Wars'. How many <code>id</code>s correspond to this name in the themes.csv? Now use these <code>id</code>s and find the corresponding the sets in the sets.csv (Hint: you'll need to look for matches in the <code>theme_id</code> column)
import pandas as pd

themes_df = pd.read_csv("data/themes.csv")

print(f"First 5\n{themes_df.head()}\n")
print(f"Last 5\n{themes_df.tail()}")

# add .values to exclude index
star_wars_id  = themes_df.loc[themes_df['name'] == 'Star Wars', 'id'].values
print(star_wars_id)
sets_df = pd.read_csv("data/sets.csv")
# sets_df['theme_id'] goes to the theme_id in sets_df and then checks 
# if start_wars_id is in theme_id and if there it filters from sets_df to create new_df
star_wars_sets = sets_df[sets_df['theme_id'].isin(star_wars_id)]
print(star_wars_sets)


### Merging (i.e., Combining) DataFrames based on a Key

# Merge sets_df with themes_df using theme_id (sets_df) and id (themes_df)
# left_on and right_on matches the id
merged_df = sets_df.merge(themes_df, left_on='theme_id', right_on='id')

# Show the first few rows to verify the merge
print(merged_df.head())
# Count unique themes per year
themes_per_year = merged_df.groupby('year')['theme_id'].nunique()

# Count total sets per year
sets_per_year = merged_df.groupby('year')['set_num'].count()

import matplotlib.pyplot as plt

# Create figure
fig, ax1 = plt.subplots(figsize=(12, 6))

# First y-axis (number of sets)
ax1.plot(sets_per_year.index, sets_per_year, color='b', linestyle='-', label="Number of Sets")
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Sets", color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Create a second y-axis for number of themes
ax2 = ax1.twinx()  # Share the same x-axis
ax2.plot(themes_per_year.index, themes_per_year, color='r', linestyle='-', label="Number of Themes")
ax2.set_ylabel("Number of Themes", color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Add title & grid
plt.title("Number of LEGO Sets & Themes Released Per Year")
ax1.grid(True)

plt.show()
