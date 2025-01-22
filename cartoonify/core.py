# core.py

import cv2

def cartoonify(image, sigma_color=75, sigma_space=75, edge_block_size=9, edge_c=9):
    """
    Converts an image to a cartoonized version.
    
    Parameters:
        image (numpy.ndarray): Input image (BGR format).
        sigma_color (int): Smoothing intensity for bilateral filter.
        sigma_space (int): Spatial intensity for bilateral filter.
        edge_block_size (int): Block size for adaptive thresholding.
        edge_c (int): Constant for adaptive thresholding.
        
    Returns:
        cartoon (numpy.ndarray): Cartoonized image.
    """
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply median blur to reduce noise
    gray = cv2.medianBlur(gray, 5)

    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, edge_block_size, edge_c
    )

    # Apply bilateral filter for smoothing while preserving edges
    color = cv2.bilateralFilter(image, d=9, sigmaColor=sigma_color, sigmaSpace=sigma_space)

    # Combine the edges with the smoothed image
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon
