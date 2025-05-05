# statistical.py

from PIL import Image
from math import log2
from scipy.stats import chisquare

def get_histogram(img):
    """
    Convert the image to grayscale and return its histogram.
    """
    grayscale = img.convert("L")  # Convert to grayscale
    hist = grayscale.histogram()  # 256 bins for pixel values 0-255
    return hist

def calculate_entropy(img):
    """
    Calculate the entropy of the image based on grayscale histogram.
    """
    hist = get_histogram(img)
    total_pixels = sum(hist)
    entropy = 0

    for count in hist:
        if count > 0:
            probability = count / total_pixels
            entropy -= probability * log2(probability)

    return entropy

def chi_square_test(img):
    """
    Perform a chi-square test on the grayscale histogram to assess uniformity.
    """
    hist = get_histogram(img)
    total = sum(hist)
    num_bins = len(hist)

    # Uniform expected distribution
    expected = [total / num_bins] * num_bins

    # Chi-square test
    chi_stat, p_value = chisquare(f_obs=hist, f_exp=expected)

    return chi_stat, p_value


