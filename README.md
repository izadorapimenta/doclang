# Language Identification with NLTK

This Python script uses the NLTK library along with langid to identify the languages in a given text and count the number of sentences in each language. It reads text from a DOCX file, tokenizes it into sentences, identifies the language of each sentence, and provides a count for each identified language.

## Requirements

- Python 3.x
- NLTK
- langid
- python-docx

Install the required Python packages using the following command:

```bash
pip install langid nltk python-docx
```

## Usage

- Clone the repository:

```bash
git clone https://github.com/izadorapimenta/doclang.git
cd doclang
```

- Replace the docx_file_path variable in the script with the path to your DOCX file.

- Run the script:

```bash
python doclang.py
```

## Example

Suppose you have a DOCX file (doclang.docx) with mixed Portuguese and Italian sentences. After running the script, it will output:

```bash
Number of sentences in pt: 2
Number of sentences in it: 1
```

Feel free to customize the example text in the script for your specific use case.


