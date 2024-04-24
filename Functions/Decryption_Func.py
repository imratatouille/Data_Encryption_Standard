from Functions.Permutation_Func import initial_permutation, inverse_permutation
from Functions.Round_Func import round_Func
from Functions.Generate_keys_Func import generate_subkeys
from Functions.String_To_Binary_Func import string_to_binary

def decryption(CT, KEY):
    key_change_to_bin = string_to_binary(f"{KEY}")
    subkeys = generate_subkeys(key=key_change_to_bin)

    IP_Cb = initial_permutation(CT)

    Left_Cb = IP_Cb[:32]
    Right_Cb = IP_Cb[32:]

    for i in range(16):
        Left_Cb, Right_Cb = round_Func(Right_Cb, Left_Cb, subkeys[15-i])

    Byte = Left_Cb + Right_Cb

    IP_Byte = inverse_permutation(Byte)
    
    return IP_Byte