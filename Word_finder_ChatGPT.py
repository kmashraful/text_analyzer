#!/usr/bin/env python
# coding: utf-8

# In[ ]:


####################### TEXT ANALYZER ##########################



###############################################################


# In[ ]:


## USER DEFINES:
# File name and location:

file_name = 'FSEP_LEcology'
folder_path = r'C:\Users\DELL\Documents\OSU\Extra Paper\Geo Chat GPT\Python codes\Docket'


# In[ ]:


# Libraries and modules
import os
import PyPDF2
import pandas as pd
from fuzzywuzzy import process


# In[ ]:


# Word list (Lobben, A., & Lawrence, M. (2015). Synthesized Model of Geospatial Thinking. The Professional Geographer, 67(3), 307–318. https://doi.org/10.1080/00330124.2014.935155)
simple = ['adjacency', 'arrangement', 'boundary', 'class', 'connection', 'direction', 'distance', 'distribution', 'edge', 'enclosure', 'movement', 'order', 'proximity', 'reference frame', 'region', 'sequence', 'shape', 'transition']
difficult = ['adjacency', 'angle', 'area', 'center', 'change', 'cluster', 'grid', 'growth', 'isolated', 'linked', 'polygon', 'reference frame', 'spread']
complicated = ['buffer', 'connectivity', 'corridor', 'gradient', 'profile', 'representation', 'scale', 'surface']
complex_ = ['activity space', 'association', 'buffer', 'central place', 'cluster', 'density', 'diffusion', 'distortion', 'distribution', 'dominance', 'enclave', 'gradient', 'great circle', 'hierarchy', 'interpolation', 'layer', 'network', 'overlay', 'pattern', 'profile', 'projection', 'relief', 'scale', 'social area', 'subjective space']


# In[ ]:


# Combine all lists into one
all_words = simple + difficult + complicated + complex_

# Initialize a dictionary to store unique words
unique_words_dict = {}

# Iterate over each list and remove duplicates found in previous columns
for col, words in zip(['Simple', 'Difficult', 'Complicated', 'Complex'], [simple, difficult, complicated, complex_]):
    unique_words = []
    for word in words:
        # Check if the word is not already in previous columns
        if word not in unique_words_dict:
            unique_words_dict[word] = col
            unique_words.append(word)
    unique_words_dict.update({word: col for word in words})
    unique_words_dict.update({word: col for word in words})
    unique_words_dict.update({word: col for word in words})
    unique_words_dict.update({word: col for word in words})
    unique_words_dict.update({word: col for word in words})
    unique_words_dict.update({word: col for word in words})
    unique_words_dict.update({word: col for word in words})
    unique_words_dict.update({word: col for word in words})
    unique_words_dict.update({word: col for word in words})
    unique_words_dict.update({word: col for word in words})
    unique_words_dict.update({word: col for word in words})
    unique_words_dict.update({word: col for word in words})
    unique_words_dict.update({word: col for word in words})
    

# Create DataFrame
df_word = pd.DataFrame(unique_words_dict.items(), columns=['Keywords', 'Category'])

df_word


# In[ ]:


# # Additional
# df = df_word.sort_values(by= 'Keywords')
# df


# In[ ]:


# Min and maximum characters in keywords
min_length = df_word['Keywords'].str.len().min()
max_length = df_word['Keywords'].str.len().max()
print("Minimum length of words:", min_length)
print("Maximum length of words:", max_length)


# In[ ]:


# Function to find matches for a word in the PDF
def find_matches(word, page_num, line_num):
    if len(word) < 4:  # Ignore words less than 4 characters long
        return None
    matches = process.extractOne(word, df_word['Keywords'], score_cutoff=80)
    if matches:
        matched_word = matches[0]
        category = df_word[df_word['Keywords'] == matched_word]['Category'].values[0]
        score = matches[1]
        return {
            'Word': word,
            'Matched Word': matched_word,
            'Category': category,
            'Page Number': page_num + 1,  # Adding 1 because page numbers start from 0
            'Line Number': line_num+1, # Adding 1 because line numbers start from 0
            'Fuzzy Match Score': score
        }
    else:
        return None

# Function to read PDF (which is ChatGPT's answer) and find matches
def find_matches_in_pdf(pdf_path):
    matches_found = []
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text = page.extractText().split('\n')  # Split text into lines
            for line_num, line_text in enumerate(text):
                words = line_text.split()  # Split line into words
                for word in words:
                    word = word.strip().lower()  # Convert to lowercase and remove leading/trailing spaces
                    match = find_matches(word, page_num, line_num)
                    if match:
                        matches_found.append(match)
    return matches_found

# Concatenate file name and location
pdf_path = os.path.join(folder_path, file_name + '.pdf')
matches = find_matches_in_pdf(pdf_path)

# Convert matches to DataFrame
df_matches = pd.DataFrame(matches)

# Display DataFrame
df_matches


# In[ ]:


# Word count function
def get_pdf_word_count(pdf_path):
    # Open the PDF file in binary mode
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        # Initialize a variable to store the total word count
        total_words = 0

        # Loop through all the pages in the PDF
        for page_num in range(pdf_reader.numPages):
            # Extract text from the current page
            page_text = pdf_reader.getPage(page_num).extractText()

            # Split the text into words, ignoring white spaces, and update the total word count
            words = page_text.split()
            total_words += sum(len(word.strip()) > 0 for word in words)

    return total_words


total_words = get_pdf_word_count(pdf_path)

# Display the total word count
print("Total Words in PDF:", total_words)


# In[ ]:


# Export as a csv
df_matches.to_csv(file_name+' document analysis report'+ ' for total words of ' + str(total_words) + ' '+ '.csv', index=False)

