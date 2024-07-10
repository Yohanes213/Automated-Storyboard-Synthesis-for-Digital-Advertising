import pytesseract
import logging
from PIL import Image

logging.basicConfig(level=logging.INFO)


def extract_text_on_image(image_location):
    try:
        text = pytesseract.image_to_string(Image.open(image_location))
        logging.info('Text extracted from image successfully.')
        return text
    except Exception as e:
        logging.error(f"An unexpected error occurred while extracting text from image: {e}")
        return []
    
