from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(image_path):
    try:
        image = Image.open(image_path)
        exifdata = image.getexif()
        metadata = {}
        for tag_id, value in exifdata.items():
            tag = TAGS.get(tag_id, tag_id)
            metadata[tag] = value
        return metadata
    except Exception as e:
        return {"Error": str(e)}
