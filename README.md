# Regular Expression Onboarding Hackathon
This hackathon is about the project of extracting data like emails, phone numbers, Hashtags, URLs, HTML tags, and currencies using Regular expressions by designing an API responsible for that task.

# Setup Instructions
## Prerequisites
   * Python 3
   * Flask
## Cloning the repository
```python
git clone https://github.com/userName/alu_regex-data-extraction_userName.git
cd alu_regex-data-extraction_userName
```
## Writing Scripts that will extract the data
1. [data_file.py](https://github.com/ai-ngabo/alu_regex-data-extraction_ai-ngabo/blob/main/use-python/data_file.py)
2. [extract.py](https://github.com/ai-ngabo/alu_regex-data-extraction_ai-ngabo/blob/main/use-python/extract.py)

# Usage
## 1. Run the app
```bash
python3 extract.py
```
## 2. Access the API
`http://127.0.0.1:5000/extract-data`
## Extracting Data from a File
```bash
curl -X POST -H "Content-Type: application/json" -d '{"file_path": "data.csv"}' http://127.0.0.1:5000/extract-data
## Project Structure
```
## Project Structure
```
data-extraction-api/
 ├── data_file.py       # Contains sample data          
 ├── extract.py         # Main script for running the Flask API and data 
 extraction
 └── README.md          # Project documentation
 ```
## API Endpoints
*/extract-data [GET]
-*Description*: Extracts data from the provided text file.
-*Response*: JSON object containing extracted data.

*/extract-data [POST]
-**Description**: Extracts data from the provided file path sent in the request body.
-**Request Body**: JSON object containing the file path.
```json
{
  "file_path": "data_file.py"
}
```
## Contact
* **Name**: Alain NGABO
* **Email**: a.ngabo@alustudent.com
* **Github**: [ai-ngabo](https://github.com/ai-ngabo)
