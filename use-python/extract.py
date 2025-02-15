#!/usr/bin/python3

import re
from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to read the file and extract data
def extract_data(file_path):
    try:
        # Read the text file
        with open(file_path, "r") as file:
            text = file.read()

        # Email extraction
        email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        emails = re.findall(email_regex, text)

        # URL extraction
        url_regex = r"https?:\/\/(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\/[^\s]*)?"
        urls = re.findall(url_regex, text)

        # Phone number extraction
        phone_regex = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
        phones = re.findall(phone_regex, text)

        # Currency extraction
        currency_regex = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
        prices = re.findall(currency_regex, text)

        # Hashtag extraction
        hashtag_regex = r"#\w+"
        hashtags = re.findall(hashtag_regex, text)

        # Return extracted data in a dictionary
        return {
            "emails": emails,
            "urls": urls,
            "phones": phones,
            "prices": prices,
            "hashtags": hashtags
        }

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return {}

@app.route('/extract-data', methods=['POST'])
def extract_data_api():
    file_path = request.json.get('file_path')
    if not file_path:
        return jsonify({"error": "No file path provided"})

    extracted_data = extract_data(file_path)
    if not extracted_data:
        return jsonify({"error": "No text data found in the file"})

    return jsonify(extracted_data)

if __name__ == '__main__':
    # Assigning file_path to the exact file containing the data to extract
    file_path = "data.csv"
    extracted_data = extract_data(file_path)

    # printing the output
    if extracted_data:
        print("-" * 40)
        print("Extracted Data:")
        print("Emails:", extracted_data["emails"])
        print("URLs:", extracted_data["urls"])
        print("Phone Numbers:", extracted_data["phones"])
        print("Prices:", extracted_data["prices"])
        print("Hashtags:", extracted_data["hashtags"])
        print("-" * 40)

        #save results to a new file as an offline backup
        with open("extracted_data.txt", "w") as output_file:
            for key, data in extracted_data.items():
                output_file.write(f"{key.capitalize()}:\n")
                output_file.write("\n".join(data) + "\n\n")

    # Run the Flask app
    app.run(debug=True)

