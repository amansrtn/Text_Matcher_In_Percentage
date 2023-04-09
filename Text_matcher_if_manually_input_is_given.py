import numpy as np
import csv
import difflib

threshold = 0.8
output = 0
# read the CSV file
with open('women_safety_dataset.csv', 'r') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]

# input from server
server_text = "ill scream if you follow any closer"

# matching of data
for row in rows:
    your_data = row['Message']
    matcher = difflib.SequenceMatcher(None, server_text, your_data)
    score = matcher.ratio()
    if score >= threshold:
        output = 1
        break
print("Prediction = ", output)
