import cv2

def load_image(image_path):
    """Loads an image from a file path."""
    # Load the image from the given path (returns None if the path is invalid)
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image from {image_path}")
    return image

def save_image(image, output_path):
    """Saves an image to a file."""
    # Save the image to the specified path (returns True on success, False on failure)
    success = cv2.imwrite(output_path, image)
    if success:
        print(f"Image saved successfully to {output_path}")
    else:
        print(f"Error: Failed to save image to {output_path}")
