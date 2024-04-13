#!/usr/bin/env python
# coding: utf-8

# In[ ]:


####################### PLOTTING ##########################



###############################################################


# In[ ]:


### USER DEFINES:
# File name and location:

file_name = 'ZSP_LEcology'
# Define color of plot
defined_color = 'seagreen' # can be 'tomato'

# Directory:
folder_path = r'C:\Users\DELL\Documents\OSU\Extra Paper\Geo Chat GPT\Python codes\Analysis'


# In[ ]:


# Libraries and modules
import os
import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:


# List to store matching CSV filenames
matching_files = []

# Iterate over all files in the folder_path
for filename in os.listdir(folder_path):
    # Check if the file is a CSV file
    if filename.endswith('.csv'):
        # Check if the filename starts with a specific term
        if filename.startswith(file_name):
            # If it does, add it to the list
            matching_files.append(filename)

# Print the matching filenames
print("Matching CSV files:", matching_files)


# In[ ]:


# Concatenate file name and location
csv_path = os.path.join(folder_path, matching_files[0])
# Read the CSV file into a DataFrame
df = pd.read_csv(csv_path)


# In[ ]:


# Number of keywords grouped by categories:
category_counts = df.groupby('Category').size().reset_index(name='Count')

# Display on console:
category_counts


# In[ ]:


# Ensure all categories are present with a count of 0 if missing
all_categories = ['Complex', 'Complicated', 'Difficult', 'Simple']
missing_categories = list(set(all_categories) - set(category_counts['Category']))
missing_data = pd.DataFrame({'Category': missing_categories, 'Count': [0] * len(missing_categories)})
category_counts = pd.concat([category_counts, missing_data])

# Sort the DataFrame by category for consistency
category_counts = category_counts.sort_values(by='Category')
category_counts


# In[ ]:


# Data
categories = category_counts['Category']
counts = category_counts['Count']

# Reverse the order of categories
categories = categories[::-1]
counts = counts[::-1]

# Create bar plot
plt.figure(figsize=(8, 6))
bars = plt.bar(categories, counts, color=defined_color)

# Adding labels and title
plt.xlabel('Geospatial lexicons by complexity')
plt.ylabel('Count')
plt.title(' ')
plt.xticks(rotation=45)

# Set y-axis limits and format ticks
plt.ylim(0, 30)  # Set the y-axis limits from 0 to 30
plt.yticks(range(0, 31))  # Set y-axis ticks from 0 to 20

# Add counts on top of each bar
for bar, count in zip(bars, counts):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), count,
             ha='center', va='bottom')

# Display the plot
plt.tight_layout()

# Save the plot
plt.savefig(file_name + ' plot.png', dpi=300)

plt.show()

