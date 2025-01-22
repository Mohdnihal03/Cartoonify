from cartoonify.utils import load_image, save_image
from cartoonify.core import cartoonify
import cv2

# Load an image
input_image_path = 'load_image'
image = load_image(input_image_path)

if image is not None:
    # Apply cartoonification if the image loaded successfully
    cartoon_image = cartoonify(image)

    # Save the cartoonified image
    output_image_path = 'cartoon_example.jpg'
    save_image(cartoon_image, output_image_path)

    # Optionally display the result
    cv2.imshow('Cartoon Image', cartoon_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
