import unittest
import numpy as np
from PIL import Image

import sys
import os

sys.path.append(os.path.abspath(os.path.join("../Automated-Storyboard-Synthesis-for-Digital-Advertising/scripts")))
from image_compose import extract_text_on_image, resize_to_fit, combine_images_grid

class TestImageProcessing(unittest.TestCase):

    def test_resize_to_fit(self):
        # Create a sample image
        image = np.random.randint(0, 255, (100, 200, 3), dtype=np.uint8)

        # Test various resize scenarios
        resized_image = resize_to_fit(image, 50, 150)
        self.assertEqual(resized_image.shape[0], 50)
        self.assertEqual(resized_image.shape[1], 100)

        resized_image = resize_to_fit(image, 200, 300)
        self.assertEqual(resized_image.shape[0], 100)
        self.assertEqual(resized_image.shape[1], 200)

        # Test if image is not resized when dimensions are smaller
        resized_image = resize_to_fit(image, 150, 300)
        self.assertEqual(resized_image.shape, image.shape)

    def test_combine_images_grid(self):
        # Create sample images
        base_image = np.zeros((300, 300, 3), dtype=np.uint8)
        overlay1 = np.ones((100, 100, 3), dtype=np.uint8) * 255
        overlay2 = np.ones((50, 50, 3), dtype=np.uint8) * 128

        # Test basic placement
        overlays = [(overlay1, (0, 0)), (overlay2, (1, 2))]
        combined_image = combine_images_grid(base_image, overlays)

        # Assert that overlays are placed correctly (basic check)
        self.assertTrue(np.array_equal(combined_image[0:100, 0:100], overlay1))


if __name__ == '__main__':
    unittest.main()
