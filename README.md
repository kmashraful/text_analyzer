# **Text Analyzer for Finding Geography-Related Lexicons**

## _Purpose:_

This Python script serves as a text analyzer tailored for examining geography-related lexicons within textual content. It was specifically developed for a project titled "Assessing How ChatGPT Handles the Complexities of Scale through the Lens of Geography," which investigates how ChatGPT, a language model developed by OpenAI, handles geographical concepts. The results are shared in American Association of Geographers (AAG) 2024.

## _How it Works:_

Keyword Compilation: The script begins by compiling a list of geography-related keywords categorized into four groups: Simple, Difficult, Complicated, and Complex. These keywords are sourced from academic literature (Lobben, A., & Lawrence, M. (2015). Synthesized Model of Geospatial Thinking. The Professional Geographer, 67(3), 307–318. https://doi.org/10.1080/00330124.2014.935155
).

PDF Text Analysis: It then analyzes textual content, typically sourced from PDF documents, searching for occurrences of the compiled keywords. Using fuzzy string matching techniques, it identifies matches between words in the text and keywords in the lexicon, considering variations and misspellings.

Reporting: Matches are recorded along with their respective categories, page numbers, and line numbers within the document. Additionally, the script provides insights such as total word count of the analyzed document.

Exporting Results: Finally, the script exports the analysis results to a CSV file.

## _Usage:_

Customization: Users can customize the script by providing their own PDF document and adjusting parameters such as file paths and fuzzy matching thresholds.

Interpretation: The generated CSV report enables users to assess the presence of geography-related lexicons within the analyzed text, shedding light on the model's comprehension and usage of geographical concepts.
