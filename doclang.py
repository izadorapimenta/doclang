import langid
import nltk
from nltk.tokenize import sent_tokenize
from docx import Document

# Download NLTK data for sentence tokenization
nltk.download('punkt')

def identify_language(sentence):
    # Use langid to identify the language of a sentence
    lang, _ = langid.classify(sentence)
    return lang

def count_sentences_by_language(sentences):
    # Initialize counters for each language
    language_counts = {}

    # Identify the language of each sentence and count
    for sentence in sentences:
        lang = identify_language(sentence)

        # Increment the corresponding counter
        if lang in language_counts:
            language_counts[lang] += 1
        else:
            language_counts[lang] = 1

    return language_counts

def read_text_from_docx(file_path):
    # Read text from a DOCX file
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + " "
    return text

if __name__ == "__main__":
    # Replace the file path with your own DOCX file path
    docx_file_path = "docx_file_path"

    # Read text from the DOCX file
    text_from_docx = read_text_from_docx(docx_file_path)

    # Tokenize the text into sentences
    sentences = sent_tokenize(text_from_docx)

    # Identify languages and count sentences by language
    language_counts = count_sentences_by_language(sentences)

    # Print the results
    for lang, count in language_counts.items():
        print(f"Number of sentences in {lang}: {count}")
