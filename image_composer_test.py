import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from autogen import Agent

def compose_ad_frame(assets_folder, concept_data):
    """
    Composes an advertisement frame using assets and concept data.
    
    Parameters:
    - assets_folder (str): Path to the folder containing image assets.
    - concept_data (dict): Data describing the concept and assets for the frame.
    
    Returns:
    - PIL.Image.Image: Composed advertisement frame.
    """
    # Initialize a blank canvas for the ad frame
    frame = Image.new('RGB', (600, 400), color='white')
    draw = ImageDraw.Draw(frame)
    
    # Load and paste landing and endframe images
    landing_image = Image.open(os.path.join(assets_folder, '0a59be2e7dd53d6de11a10ce3649c081/landing_1.png'))
    endframe_image = Image.open(os.path.join(assets_folder, '0a59be2e7dd53d6de11a10ce3649c081/end-1.jpg'))
    frame.paste(landing_image, (0, 0))
    frame.paste(endframe_image, (400, 0))
    
    # Example of manually setting text and color
    font = ImageFont.load_default()
    draw.text((50, 50), concept_data['text'], font=font, fill='black')
    primary_color = concept_data['primary_color']
    draw.rectangle([(0, 0), (200, 100)], fill=primary_color)
    
    return frame

# Example usage
assets_folder = 'data'
concept_data = {
    'text': 'Sample advertisement text',
    'primary_color': '#FF0000'
}

#composed_frame = compose_ad_frame(assets_folder, concept_data)
#composed_frame.show()
#composed_frame.save('hell.jpg')
