
# Extract and Translate

## Overview
This script extracts text from a DOCX file, translates it to another language using Google Translate, and saves the translated content to a new file.

## Prerequisites
- Python 3
- Required Python packages listed in `requirements.txt`

## Installation
1. Clone the repository.
2. Create a virtual environment (optional but recommended).
3. Install dependencies using `pip install -r requirements.txt`.

## Usage
Run the script by providing the path to the input DOCX file. Optionally, specify the output file, input language, and output language.

Example usage:
```bash
python extract_and_translate.py -f input_file.docx -o output_file.md -il en -ol fr
```
Alternatively:
```bash
chmod +x extract_and_translate.py
./extract_and_translate.py -f input_file.docx -o output_file.md -il en -ol fr
```
Add to path:
```bash
echo 'export PATH="$PATH:'"$PWD"'"' >> ~/.bashrc
```
