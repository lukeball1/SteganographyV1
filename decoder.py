import argparse
from PIL import Image
from util import *

def decode_message_in_image(image_path):
    # Load the image
    image = Image.open(image_path)
    image = image.convert("RGB")
    pixels = image.load()
    
    bits = []
    width, height = image.size
    
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            bits.append(str(r & 1))
            bits.append(str(g & 1))
            bits.append(str(b & 1))
            
    # Convert the bits to message
    bit_str = ''.join(bits)
    message = bits_to_message(bit_str)
    return message

#for individual use and testing purposes
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract a hidden message from an image.")
    parser.add_argument("input_image", help="Path to the encoded image file")
    args = parser.parse_args()

    hidden_message = decode_message_in_image(args.input_image)
    print("Decoded message:")
    print(hidden_message)