#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PDF Processor

This module provides functionality to extract text from PDF files and convert it to markdown format.
It can be used as a standalone script or imported as a module.

Usage as a script:
    python pdf_processor.py input.pdf output.md

Usage as a module:
    from pdf_processor import PDFProcessor
    processor = PDFProcessor()
    markdown_text = processor.pdf_to_markdown('input.pdf')
    with open('output.md', 'w') as f:
        f.write(markdown_text)
"""

import sys
import re
import argparse
from typing import List, Dict, Tuple, Optional, Union


class PDFProcessor:
    """
    A class for processing PDF files and converting them to markdown format.
    """

    def __init__(self):
        """Initialize the PDFProcessor."""
        pass

    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """
        Extract text from a PDF file.

        Args:
            pdf_path: Path to the PDF file.

        Returns:
            Extracted text from the PDF.
        """
        try:
            import PyPDF2
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    text += page.extract_text()
                return text
        except ImportError:
            print("PyPDF2 is not installed. Trying pdftotext...")
            return self._extract_text_using_pdftotext(pdf_path)

    def _extract_text_using_pdftotext(self, pdf_path: str) -> str:
        """
        Extract text from a PDF file using pdftotext command-line tool.

        Args:
            pdf_path: Path to the PDF file.

        Returns:
            Extracted text from the PDF.
        """
        import subprocess
        import tempfile
        
        with tempfile.NamedTemporaryFile(suffix='.txt') as temp_file:
            try:
                subprocess.run(['pdftotext', pdf_path, temp_file.name], check=True)
                with open(temp_file.name, 'r') as f:
                    return f.read()
            except (subprocess.SubprocessError, FileNotFoundError):
                print("Error: pdftotext command failed. Make sure it's installed.")
                print("On Ubuntu/Debian: sudo apt-get install poppler-utils")
                print("On macOS: brew install poppler")
                return ""

    def clean_text(self, text: str) -> str:
        """
        Clean the extracted text by removing excessive whitespace and normalizing line breaks.

        Args:
            text: The text to clean.

        Returns:
            Cleaned text.
        """
        # Remove excessive line breaks
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        # Normalize whitespace
        text = re.sub(r' +', ' ', text)
        
        # Fix hyphenated words that were split across lines
        text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', text)
        
        return text

    def convert_to_markdown(self, text: str) -> str:
        """
        Convert the cleaned text to markdown format.

        Args:
            text: The text to convert.

        Returns:
            Markdown formatted text.
        """
        # Convert section headers
        text = re.sub(r'^([IVX]+\.\s+.+)$', r'## \1', text, flags=re.MULTILINE)
        text = re.sub(r'^([0-9]+\.\s+.+)$', r'### \1', text, flags=re.MULTILINE)
        text = re.sub(r'^([A-Z][a-z]+\s+[0-9]+\.\s+.+)$', r'### \1', text, flags=re.MULTILINE)
        
        # Convert subsection headers
        text = re.sub(r'^([A-Z]\.\s+.+)$', r'#### \1', text, flags=re.MULTILINE)
        
        # Format equations (simple approach)
        text = re.sub(r'\$(.+?)\$', r'$\1$', text)
        
        # Format references
        text = re.sub(r'^\[([0-9]+)\](.+)$', r'- [\1]\2', text, flags=re.MULTILINE)
        
        # Format figures and tables
        text = re.sub(r'^(Fig\.\s+[0-9]+:)(.+)$', r'**\1**\2', text, flags=re.MULTILINE)
        text = re.sub(r'^(Table\s+[0-9]+:)(.+)$', r'**\1**\2', text, flags=re.MULTILINE)
        
        # Format definitions, theorems, lemmas
        text = re.sub(r'^(Definition\s+[0-9]+:)(.+)$', r'**\1**\2', text, flags=re.MULTILINE)
        text = re.sub(r'^(Theorem\s+[0-9]+:)(.+)$', r'**\1**\2', text, flags=re.MULTILINE)
        text = re.sub(r'^(Lemma\s+[0-9]+:)(.+)$', r'**\1**\2', text, flags=re.MULTILINE)
        
        return text

    def pdf_to_markdown(self, pdf_path: str) -> str:
        """
        Process a PDF file and convert it to markdown.

        Args:
            pdf_path: Path to the PDF file.

        Returns:
            Markdown formatted text.
        """
        text = self.extract_text_from_pdf(pdf_path)
        cleaned_text = self.clean_text(text)
        markdown_text = self.convert_to_markdown(cleaned_text)
        return markdown_text


def main():
    """Main function to run the script."""
    parser = argparse.ArgumentParser(description='Convert PDF to Markdown')
    parser.add_argument('input', help='Input PDF file')
    parser.add_argument('output', nargs='?', help='Output Markdown file (optional)')
    
    args = parser.parse_args()
    
    processor = PDFProcessor()
    markdown_text = processor.pdf_to_markdown(args.input)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(markdown_text)
        print(f"Markdown saved to {args.output}")
    else:
        print(markdown_text)


if __name__ == "__main__":
    main()
