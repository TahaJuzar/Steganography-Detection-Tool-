from PIL import Image

def extract_lsb_data(image_path, num_bits=None):
    img = Image.open(image_path)
    pixels = list(img.getdata())
    bits = []

    for pixel in pixels:
        for channel in pixel[:3]:  # R, G, B
            bits.append(channel & 1)

            if num_bits and len(bits) >= num_bits:
                break
        if num_bits and len(bits) >= num_bits:
            break

    # Convert bits to bytes
    bytes_data = bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for b in bits[i:i+8]:
            byte = (byte << 1) | b
        bytes_data.append(byte)

    return bytes_data

if __name__ == "__main__":
    data = extract_lsb_data("testimage3.jpeg")
    with open("extracted.bin", "wb") as f:
        f.write(data)
    print("🔍 Extraction complete: saved as extracted.bin")
