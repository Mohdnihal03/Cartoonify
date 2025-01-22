# tests/test_cartoonify.py

import pytest
import cv2
from cartoonify.core import cartoonify

def test_cartoonify():
    # Load a test image (you can use any image for testing)
    test_image = cv2.imread("path_to_your_test_image.jpg")  # Replace with an actual test image path

    # Apply the cartoonify function
    result = cartoonify(test_image)

    # Assert that the result is a valid output (e.g., not None)
    assert result is not None
    assert isinstance(result, cv2.UMat)  # UMat is used by OpenCV when handling images
