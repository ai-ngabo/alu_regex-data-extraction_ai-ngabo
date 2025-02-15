#!/usr/bin/python3

import re
from flask import Flask, request, jsonify
import data_file  # Import your data file

app = Flask(__name__)

# Function to read and extract data from the text
def extract_data(text):
    # Email extraction
    email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_regex, text)

    # URL extraction (handle malformed URLs with/without protocols)
    url_regex = r"https?:\/\/(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\/[^\s]*)?|www\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\/[^\s]*)?"
    urls = re.findall(url_regex, text)

    # Phone number extraction (handle multiple formats)
    phone_regex = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}|\d{3}[-.\s]\d{3}[-.\s]\d{4}"
    phones = re.findall(phone_regex, text)

    # Currency extraction (handle multiple formats)
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

@app.route('/extract-data', methods=['GET'])
def extract_data_api():
    # Ensure the text data is loaded correctly from data_file
    text = data_file.paragraph
    extracted_data = extract_data(text)
    
    if not extracted_data:
        return jsonify({"error": "No text data found"}), 404

    return jsonify(extracted_data)

if __name__ == '__main__':
    #running the app
    app.run(debug=True)

