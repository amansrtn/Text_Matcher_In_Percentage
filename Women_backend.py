import json
from flask import Flask, request
import csv
import difflib

app = Flask(__name__)

with open('women_safety_dataset.csv', 'r') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]

output = "Done Succesfully"
threshold = 0.8


@app.route('/', methods=['GET', 'POST'])
def predict():
    if(request.method == 'POST'):

        global output
        output = 0
        request_data = request.data
        request_data = json.loads(request_data.decode('Utf-8'))
        input_list = request_data['Message']

        for row in rows:
            your_data = row['Message']
            matcher = difflib.SequenceMatcher(None, input_list, your_data)
            score = matcher.ratio()
            if score >= threshold:
                output = 1
                break
        return str(output)
    else:
        return str(output)


if __name__ == "__main__":
    app.run()
