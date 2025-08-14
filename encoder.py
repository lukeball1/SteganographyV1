import argparse
from PIL import Image
from util import *

def encode_message_in_image(image_path, ending_path, message):
    # Load the image
    image = Image.open(image_path)
    image = image.convert("RGB")
    pixels = image.load()
    
    # Convert message to bits
    message += chr(0) #null character to know when to stop
    message_Bits = message_to_bits(message)
    bit_index = 0
    
    # image.size is a 2-tuple 
    height, width = image.size
    
    for y in range(height):
        for x in range(width):
            #exit condition
            if (bit_index >= len(message_Bits)):
                break
            
            r, g, b = pixels[x, y]
            r = (r & ~1) | int(message_Bits[bit_index])
            bit_index += 1
            
            if (bit_index < len(message_Bits)):
                g = (g & ~1) | int (message_Bits[bit_index])
                bit_index += 1
            
            if (bit_index < len(message_Bits)):
                b = (b & ~1) | int(message_Bits[bit_index])
                bit_index += 1
            
            pixels[x, y] = (r, g, b)
        if (bit_index >= len(message_Bits)):
            break
        
    image.save(ending_path)
    print(f'Encryption finished and can be found in {ending_path}')
    
#for individual use and testing purposes
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hide a message inside an image.")
    parser.add_argument("input_image", help="Path to the input image file")
    parser.add_argument("output_image", help="Path to save the encoded image")
    parser.add_argument("message", help="The message to hide in the image")
    args = parser.parse_args()

    encode_message_in_image(args.input_image, args.output_image, args.message)