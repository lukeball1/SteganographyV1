def message_to_bits(message):
    return ''.join(f'{ord(c):08b}' for c in message)



def bits_to_message(bits):
    chars = []
    for i in range (0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            break #incomplete byte at the end
        char = chr(int(byte, 2))
        if char == '\0':
            break
        chars.append(char)
    return ''.join(chars)


#for individual use and testing purposes
if __name__ == "__main__":
    message = input("Put message here: ")
    #message_to_bits(message)
    print(message_to_bits(message))
    print(bits_to_message(message_to_bits(message)))