import matplotlib.pyplot as plt
import numpy as np

def show_rgb_channels(img):
    r, g, b = img.split()
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))
    axs[0].imshow(r, cmap='Reds')
    axs[0].set_title("Red Channel")
    axs[1].imshow(g, cmap='Greens')
    axs[1].set_title("Green Channel")
    axs[2].imshow(b, cmap='Blues')
    axs[2].set_title("Blue Channel")
    plt.show()

def plot_histogram(img):
    np_img = np.array(img)
    colors = ('r', 'g', 'b')
    for i, color in enumerate(colors):
        hist = np.histogram(np_img[..., i], bins=256, range=(0, 256))[0]
        plt.plot(hist, color=color)
    plt.title("RGB Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.show()
