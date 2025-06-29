from PIL import Image

def encode_image(input_image_path, output_image_path, secret_message):
    image = Image.open(input_image_path)
    encoded = image.copy()
    width, height = image.size
    index = 0

    binary_message = ''.join(format(ord(i), '08b') for i in secret_message)
    binary_message += '1111111111111110'  # Delimiter to indicate end of message

    for row in range(height):
        for col in range(width):
            if index < len(binary_message):
                r, g, b = image.getpixel((col, row))
                r = (r & ~1) | int(binary_message[index])
                index += 1
                if index < len(binary_message):
                    g = (g & ~1) | int(binary_message[index])
                    index += 1
                if index < len(binary_message):
                    b = (b & ~1) | int(binary_message[index])
                    index += 1
                encoded.putpixel((col, row), (r, g, b))
            else:
                encoded.save(output_image_path)
                return True
    return False

def decode_image(image_path):
    image = Image.open(image_path)
    binary_data = ''
    width, height = image.size

    for row in range(height):
        for col in range(width):
            r, g, b = image.getpixel((col, row))
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
    decoded_message = ''
    for byte in all_bytes:
        if byte == '11111110':  # Delimiter found
            break
        decoded_message += chr(int(byte, 2))
    return decoded_message