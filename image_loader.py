from PIL import Image
import os

def load_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError("Image file not found.")
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")
        return img
    except Exception as e:
        print(f"Error loading image: {e}")
        return None
