from flask import Flask, jsonify
import re

app = Flask(__name__)

# Function to extract data from text
def extract_data(text):
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

    return {
        "emails": emails,
        "urls": urls,
        "phones": phones,
        "prices": prices,
        "hashtags": hashtags
    }

# Function to read text from the data file (text_data stored in the file)
def read_text_data(file_path="data_file.py"):
    with open(file_path, "r") as file:
        return file.read()

@app.route('/extract-data', methods=['GET'])
def extract():
    try:
        # Read text data from the data file
        text = read_text_data("data_file.py")
        
        if not text:
            return jsonify({"error": "No text data found in the file"}), 400
        
        # Extract data from the loaded text
        extracted_data = extract_data(text)
        
        return jsonify(extracted_data)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

