# from PIL import Image
# import cv2

# def preprocess_image(image_path):
#   """
#   Preprocesses an image for OCR.

#   Args:
#       image_path: Path to the image file.

#   Returns:
#       Preprocessed image in PIL format.
#   """

#   # Open the image
#   img = Image.open(image_path)

#   # Grayscale conversion (can improve OCR accuracy)
#   img = img.convert("L")

#   # Resize to a suitable size (e.g., 300 PPI)
#   width, height = img.size
#   new_width = int(width * 2 / img.dpi)
#   new_height = int(height * 2 / img.dpi)
#   img = img.resize((new_width, new_height), Image.ANTIALIAS)

#   # Binarization (thresholding) to separate text from background
#   threshold = 127  # Adjust threshold value as needed
#   img = img.point(lambda p: 0 if p < threshold else 255)

#   # Optional: Noise reduction (e.g., median filter)
#   img = cv2.medianBlur(np.array(img), 5)

#   return img

from PIL import Image
import cv2
import numpy as np

def preprocess_image(img):
    """
    Preprocesses an image for OCR.

    Args:
        img: PIL Image object.

    Returns:
        Preprocessed image in PIL format.
    """

    # Grayscale conversion (can improve OCR accuracy)
    img = img.convert("L")

    # Resize to a suitable size (e.g., 300 PPI)
    width, height = img.size
    new_width = int(width * 2)
    new_height = int(height * 2)
    img = img.resize((new_width, new_height), Image.ANTIALIAS)

    # Binarization (thresholding) to separate text from background
    threshold = 127  # Adjust threshold value as needed
    img = img.point(lambda p: 0 if p < threshold else 255)

    # Optional: Noise reduction (e.g., median filter)
    img = cv2.medianBlur(np.array(img), 5)

    return img