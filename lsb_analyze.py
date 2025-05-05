import numpy as np

def extract_lsb(img):
    data = np.array(img)
    lsb_array = data & 1  # Get LSB using bitwise AND
    return lsb_array

def show_lsb_visual(lsb_array):
    from matplotlib import pyplot as plt
    # Multiply by 255 to make the bits visible (0 -> black, 1 -> white)
    plt.imshow(lsb_array * 255, cmap='gray')
    plt.title("Visualized LSB Layer")
    plt.axis('off')
    plt.show()

