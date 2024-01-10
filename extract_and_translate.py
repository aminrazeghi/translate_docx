#!/bin/env python3
"""
File: extract_and_translate.py
Author: Amin Razeghiyadaki
Date: 2024-01-10
github: https://github.com/aminrazeghi
email: mnrzghi@gmail.com
Description: This script extracts text from a DOCX file, translates it, and saves it to a new file.
License: MIT License
"""

from docx import Document
from googletrans import Translator

import argparse
import sys

# Function to extract text from a DOCX file, translate it to English, and save it to a new file
def extract_and_translate_it_boy(file_path: str, output_file: str, input_lang: str, output_lang: str) -> None:
    # Load the DOCX file
    doc = Document(file_path)

    # Extract text from paragraphs in the document
    extracted_text_file = []
    for para in doc.paragraphs:
        extracted_text_file.append(para.text + "\n")

    # Initialize the translator
    translator = Translator()

    # Translate each line of text and create a translated content
    translated_text = ''
    for line in extracted_text_file:
        if line.strip() != '':
            chunk_trasnlated = translator.translate(line, src =input_lang, dest=output_lang).text
            translated_text += chunk_trasnlated + "\n"

    # Define the path for the translated output file
    translated_file_path = file_path.replace('.docx', '_translated.md')
    # Write the translated content to the output file
    with open(translated_file_path, 'w') as f:
        f.write(translated_text)

    print(f"Translation complete. Translated file saved as '{translated_file_path}'.")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Translate DOCX file content to English.')
    parser.add_argument('-f', '--file_path', type=str, help='Path to the input DOCX file')
    parser.add_argument('-o', '--output', type=str, help='Path to the output MD file')
    parser.add_argument('-il', '--input_lang', type=str, default='auto', help='Input language code (default: auto)')
    parser.add_argument('-ol', '--output_lang', type=str, default='en', help='Output language code (default: en)')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    # Parse command-line arguments
    args = parser.parse_args()

    # Check if input file path is provided
    if not args.file_path:
        parser.print_help()
        sys.exit()

    # Determine output file path
    if not args.output:
        output_file = args.file_path.replace('.docx', '_translated.md')
    else:
        output_file = args.output

    extract_and_translate_it_boy(args.file_path, output_file, args.input_lang, args.output_lang)

if __name__ == "__main__":
    main()
