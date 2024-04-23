import binascii

def binary_to_text(Ciper_binary):
    decimal_number_list = []

    for i in range(0, len(Ciper_binary), 8):
        byte = Ciper_binary[i:i+8]
        binary_string = ''.join(map(str, byte))
        decimal_number = int(binary_string, 2)
        decimal_number_list.append(decimal_number)
        text = bytes(decimal_number_list)
    
    plaintext_bytes = text
    text = binascii.b2a_base64(plaintext_bytes)
    
    return text