def string_to_binary(input_string):
    binary_string = ""
    for char in input_string:
        binary_char = bin(ord(char))[2:].zfill(8)
        binary_string += binary_char
    return [int(bit) for bit in binary_string]
