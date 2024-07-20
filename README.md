# LegalEase - Simplify Your Document

LegalEase is a web application built with Streamlit that simplifies legal documents. It allows users to extract text from images or PDFs, preprocess the text to remove jargon, and then summarize and paraphrase the text for easier understanding.

## Features

- Extract text from images (JPG, PNG, JPEG) using Tesseract OCR.
- Extract text from PDF files using PyMuPDF.
- Preprocess the extracted text to remove contractions, special characters, and common legal section headers.
- Simplify legal jargon using WordNet.
- Paraphrase the simplified text using a pre-trained BART model.

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/legalease.git
    cd legalease
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the Required Packages**

    ```bash
    pip install -r requirements.txt
    ```

4. **Download NLTK Data**

    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')
    ```

5. **Set the Path to Tesseract Executable**

    Make sure Tesseract OCR is installed on your system. Update the path to the Tesseract executable in `extraction.py` if needed:
    
    ```python
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ```

## Usage

1. **Run the Streamlit Application**

    ```bash
    streamlit run app.py
    ```

2. **Upload Files**

    - Choose the file type (Image or PDF).
    - Upload the respective file.
    - View the extracted text.
    - Click on the "Simplify and Summarize" button to see the simplified and summarized text.

## File Structure

- `app.py`: Main Streamlit application file.
- `extraction.py`: Contains functions to extract text from images and PDFs.
- `preprocessing.py`: Contains functions to preprocess text.
- `simplification.py`: Contains functions to simplify and paraphrase text.

## Dependencies

- `streamlit`
- `pytesseract`
- `Pillow`
- `fitz` (PyMuPDF)
- `nltk`
- `transformers`
- `torch`

## Example

1. Upload an image or PDF file.
2. Extract text from the uploaded file.
3. Preprocess, simplify, and summarize the extracted text.
4. View the final simplified and summarized text.

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
