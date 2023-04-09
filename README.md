# Text_Matcher_In_Percentage
I have recently created an API that can take input text data from a server and match it to strings in a CSV file. The matching process is performed by comparing the input text to each string in the CSV file and calculating the similarity score between them.
If the similarity score is above 80%, my API outputs 1, indicating a match, and 0 if it is below 80%.

To create this API, I have utilized Python libraries such as pandas, nltk, and scikit-learn. These libraries provide powerful tools for working with CSV files, natural language processing, and machine learning.

The process of matching the input text to the strings in the CSV file involves performing text preprocessing, tokenization, and calculating the similarity score between the input text and each string in the CSV file. The similarity score is typically calculated using techniques such as cosine similarity, Jaccard similarity, or Levenshtein distance.

Once the similarity score has been calculated, my API compares it to a threshold of 80%. If the score is above this threshold, my API outputs 1, indicating a match, otherwise it outputs 0, indicating no match.

Overall, I believe that the API I have created is a powerful tool for matching input text to strings in a CSV file with a high degree of accuracy. This tool can be useful for several applications, such as data matching for customer service, plagiarism detection, or even spam filtering.
