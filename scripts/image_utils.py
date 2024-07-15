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
    

if __name__ == "__main__":
    print(extract_text_on_image('data/0a59be2e7dd53d6de11a10ce3649c081/cta.png'))