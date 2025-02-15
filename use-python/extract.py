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
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        emails = re.findall(email_pattern, text)

        # URL extraction
        url_pattern = r"https?:\/\/(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\/[^\s]*)?"
        urls = re.findall(url_pattern, text)

        # Phone number extraction
        phone_pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
        phones = re.findall(phone_pattern, text)

        # Currency extraction
        currency_pattern = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
        prices = re.findall(currency_pattern, text)

        # Hashtag extraction
        hashtag_pattern = r"#\w+"
        hashtags = re.findall(hashtag_pattern, text)

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
        return jsonify({"error": "No file path provided"}), 400

    extracted_data = extract_data(file_path)
    if not extracted_data:
        return jsonify({"error": "No text data found in the file"}), 404

    return jsonify(extracted_data)

if __name__ == '__main__':
    # Example usage (for demonstration purposes)
    file_path = "data.csv"
    extracted_data = extract_data(file_path)

    # Output results (for demonstration purposes)
    if extracted_data:
        print("Extracted Data:")
        print("Emails:", extracted_data["emails"])
        print("URLs:", extracted_data["urls"])
        print("Phone Numbers:", extracted_data["phones"])
        print("Prices:", extracted_data["prices"])
        print("Hashtags:", extracted_data["hashtags"])

        # Optionally, save results to a new file
        with open("extracted_data.txt", "w") as output_file:
            for category, data in extracted_data.items():
                output_file.write(f"{category.capitalize()}:\n")
                output_file.write("\n".join(data) + "\n\n")

    # Run the Flask app
    app.run(debug=True)

