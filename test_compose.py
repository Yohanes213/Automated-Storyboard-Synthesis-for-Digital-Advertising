import cv2
import matplotlib.pyplot as plt

def resize_to_fit(image, max_height, max_width):
    """
    Resize an image to fit within the given dimensions while maintaining aspect ratio.

    Parameters:
    image (np.ndarray): The image to resize.
    max_height (int): The maximum height of the resized image.
    max_width (int): The maximum width of the resized image.

    Returns:
    np.ndarray: The resized image.
    """
    h, w = image.shape[:2]
    if h > max_height or w > max_width:
        scaling_factor = min(max_height / h, max_width / w)
        new_size = (int(w * scaling_factor), int(h * scaling_factor))
        return cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)
    return image

def combine_images_grid(base_image, overlays):
    """
    Combine multiple overlay images into the base image using a 3x3 grid system.

    Parameters:
    base_image (np.ndarray): The base image where overlay images will be placed.
    overlays (list of tuples): List of overlay images and their grid positions. Each tuple should be in the format
                               (overlay_image, (grid_row, grid_col)), where (grid_row, grid_col) specifies the grid cell.

    Returns:
    np.ndarray: The combined image with overlays.
    """
    # Make a copy of the base image to modify
    combined_image = base_image.copy()
    
    # Get the dimensions of the base image
    base_h, base_w = combined_image.shape[:2]
    
    # Calculate the size of each grid cell
    cell_h, cell_w = base_h // 3, base_w // 3
    
    # Iterate through the overlay images and their grid positions
    for overlay, (grid_row, grid_col) in overlays:
        # Resize the overlay to fit within the grid cell
        overlay = resize_to_fit(overlay, cell_h, cell_w)
        
        # Get the dimensions of the overlay image
        overlay_h, overlay_w = overlay.shape[:2]
        
        # Calculate the top-left corner of the grid cell
        x = grid_col * cell_w
        y = grid_row * cell_h
        
        # Place the overlay image in the center of the grid cell
        center_x = x + (cell_w - overlay_w) // 2
        center_y = y + (cell_h - overlay_h) // 2
        
        # Ensure the region is within the bounds of the base image
        if center_y + overlay_h > base_h or center_x + overlay_w > base_w:
            raise ValueError("Overlay image exceeds the bounds of the base image at the specified location.")
        
        # Place the overlay image on the base image
        combined_image[center_y:center_y+overlay_h, center_x:center_x+overlay_w] = overlay

    return combined_image


if __name__ == '__main__':

    # Paths to images
    car_image_path = 'data/0a18978cdc8b64f900b0db6a297eb99d/end-copy.jpg'
    base_image_path = 'data/0a59be2e7dd53d6de11a10ce3649c081/landing_1.png'
    cta_image_path = 'data/0a18978cdc8b64f900b0db6a297eb99d/cta.png'

    # Load the images using cv2.imread
    base_image = cv2.imread(base_image_path)
    cta_image = cv2.imread(cta_image_path)
    car_image = cv2.imread(car_image_path)

    print(type(base_image))

    # Check the loaded images dimensions
    print(f"Base image shape: {base_image.shape}")
    print(f"CTA image shape: {cta_image.shape}")
    print(f"Car image shape: {car_image.shape}")

    # Define the overlays with their grid positions
    overlays = [
        (cta_image, (0, 2)),  # Extract text from cta_image and place it in the top-right grid cell
        (car_image, (1, 1))   # Extract text from car_image and place it in the center grid cell
    ]

    # Combine the images using the grid system with text extraction
    combined_image = combine_images_grid(base_image, overlays)

    cv2.imwrite('output_image.jpg', combined_image)
