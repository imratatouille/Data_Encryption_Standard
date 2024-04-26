def binary_to_text_ascii(Ciper_binary):
    plaintext_bytes = ''
    for i in range(0, len(Ciper_binary), 8):
        byte = Ciper_binary[i:i+8]
        binary_string = ''.join(map(str, byte))
        decimal_number = int(binary_string, 2)
        text = chr(decimal_number)
        plaintext_bytes += text
            
    return plaintext_bytes

def binary_to_text_utf16(Ciper_binary):
    decimal_number_list = []
    plaintext_bytes = []
    btext = b''
    for i in range(0, len(Ciper_binary), 8):
        byte = Ciper_binary[i:i+8]
        binary_string = ''.join(map(str, byte))
        decimal_number = int(binary_string, 2)
        decimal_number_list.append(decimal_number)
        btext += decimal_number.to_bytes(1, byteorder='big')
    
    divided_sequence = [btext[i:i+2] for i in range(0, len(btext), 2)]
    for i in divided_sequence:
        texts = i.decode('utf-16')
        plaintext_bytes.append(texts)
        
    return plaintext_bytes