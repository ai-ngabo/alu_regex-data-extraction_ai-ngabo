const express =  require('express');
const bodyParser = require('body-parser');


const extract = express();
extract.use(bodyParser.json());


// Collecting all patterns of Regular expressions to use
const regex_patterns = {
  emails: /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g,
  urls: /https?:\/\/[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+(?:\/\S*)?/g,
  phoneNumbers: /(\(\d{3}\)\s?\d{3}[-.]\d{4})|(\d{3}[-.]\d{3}[-.]\d{4})/g,
  creditCards: /\b\d{4}[- ]\d{4}[- ]\d{4}[- ]\d{4}\b/g,
  time: /\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b/g,
  htmlTags: /<\/?[a-zA-Z][a-zA-Z0-9]*\b[^>]*>/g,
  hashtags: /\B#\w+/g,
  Currencies: /\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?/g
};

// Extracting data through API 
extract.post('/extract', (req, res) => {
  const paragraph = req.body.paragraph || "";
	let extractedData = {};

	for(const [key, data] of object.entries(regex_patterns)) {
	  extractedData[key] = paragraph.match(data) || [];
	}

	res.json(extractedData);
});

// Runing the server
const PORT = process.env.PORT || 5000;
extract.listen(PORT, () => console,log(`Server running on port ${PORT}`)); 
