const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();

// Regular Expressions
const regex_patterns = {
  emails: /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b/g,
  urls: /https?:\/\/[^\s]+/g,
  phoneNumbers: /(\(\d{3}\)\s?\d{3}[-.]\d{4})|(\d{3}[-.]\d{3}[-.]\d{4})/g,
  creditCards: /\b\d{4}[- ]\d{4}[- ]\d{4}[- ]\d{4}\b/g,
  time: /\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b/g,  
  hashtags: /#\w+/g,
  currencies: /\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?/g
};


// Endpoint to extract data from JSON file
app.get('/extract-from-json', (req, res) => {
  const filePath = path.join(__dirname, 'data.json');

  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).json({ error: "Error reading JSON file" });
    }

    try {
      const jsonData = JSON.parse(data);
      if (!jsonData.paragraphs || !Array.isArray(jsonData.paragraphs)) {
        return res.status(400).json({ error: "Invalid JSON format" });
      }

      const extractedResults = jsonData.paragraphs.map(paragraph => {
        let extractedData = {};
        for (const [key, pattern] of Object.entries(regex_patterns)) {
          extractedData[key] = paragraph.match(pattern) || [];
        }
        return { paragraph, extractedData };
      });

      res.json(extractedResults);
    } catch (parseError) {
      res.status(500).json({ error: "Error parsing JSON file" });
    }
  });
});

// Start the server
const PORT = process.env.PORT || 5080;
app.listen(PORT, () => console.log(`✅ Server running on port ${PORT}`));

