from PIL import Image
import pytesseract
import fitz

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_file):
    try:
        with Image.open(image_file) as img:
            # Use pytesseract to extract text from the image
            extracted_text = pytesseract.image_to_string(img)
            return extracted_text.strip()
    except Exception as e:
        print("Error extracting text from image:", e)
        return None

def extract_text_from_pdf(pdf_file):
    try:
        text = ""
        with fitz.open(pdf_file) as doc:
            for page in doc:
                # Extract text from each page of the PDF
                text += page.get_text()
        return text.strip()
    except Exception as e:
        print("Error extracting text from PDF:", e)
        return None
    
