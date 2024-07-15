from PIL import Image, ImageDraw, ImageFont
import os

def resize_image(image, size):
    return image.resize(size)

def add_text_to_image(image, text, position, font_path='arial.ttf', font_size=20, color=(255, 255, 255)):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(position, text, fill=color, font=font)
    return image

def compose_layered_image(base_image_path, components, output_path, base_image_size=None):
    base_image = Image.open(base_image_path).convert('RGBA')  # Ensure base image is in RGBA mode
    
    if base_image_size:
        base_image = resize_image(base_image, base_image_size)
    
    for component in components:
        if 'image_path' in component:
            overlay_image = Image.open(component['image_path']).convert('RGBA')  # Ensure overlay image is in RGBA mode
            if 'size' in component:
                overlay_image = resize_image(overlay_image, component['size'])
            base_image.paste(overlay_image, component['position'], overlay_image)
        elif 'text' in component:
            base_image = add_text_to_image(base_image, component['text'], component['position'], 
                                           font_path=component.get('font_path', 'arial.ttf'), 
                                           font_size=component.get('font_size', 20), 
                                           color=component.get('color', (255, 255, 255)))
    
    try:
        base_image = base_image.convert('RGB')  # Convert back to RGB mode before saving
        base_image.save(output_path)
        print(f"Layered image saved successfully at {output_path}")
    except Exception as e:
        print(f"Error saving layered image: {e}")

if __name__ == "__main__":
    image_paths = ['data/0a59be2e7dd53d6de11a10ce3649c081/cta.png',
                   'data/0a59be2e7dd53d6de11a10ce3649c081/end-1.jpg',
                   'data/0a59be2e7dd53d6de11a10ce3649c081/game_1.png']
    components = [
    {'image_path': image_paths[0], 'position': (50, 50), 'size': (200, 200)},
    {'image_path': image_paths[1], 'position': (300, 100), 'size': (150, 150)},
    {'image_path': image_paths[2], 'position': (100, 300), 'size': (200, 200)}  # Fixed this component
    ]

    base_image_path = 'data/0a18978cdc8b64f900b0db6a297eb99d/engagement_instruction_1.png'
    output_path = 'layered_image.jpg'
    base_image_size = (800, 600)  # Create a blank base image of 800x600

    compose_layered_image(base_image_path, components, output_path, base_image_size)
