from image_loader import load_image
from visualize_analyze import show_rgb_channels, plot_histogram
from lsb_analyze import extract_lsb, show_lsb_visual
from statistical import calculate_entropy, chi_square_test
from metadata_checker import extract_metadata

def main():
    image_path = "testimage3.jpeg"  # Replace with your test image
    img = load_image(image_path)
    
    if img:
        print("\n🔍 Metadata:")
        meta = extract_metadata(image_path)
        for k, v in meta.items():
            print(f"{k}: {v}")
        
        print("\n📊 Histogram:")
        plot_histogram(img)
        
        print("\n🧬 RGB Channels:")
        show_rgb_channels(img)
        
        print("\n🧫 Extracting LSB...")
        lsb = extract_lsb(img)
        show_lsb_visual(lsb)
        
        print("\n📉 Entropy:")
        entropy = calculate_entropy(img)
        print(f"Entropy: {entropy:.4f}")
        
        print("\n📈 Chi-Square Test:")
        chi, p_val = chi_square_test(img)
        print(f"Chi-Square Value: {chi:.2f}, p-value: {p_val:.4f}")

if __name__ == "__main__":
    main()
