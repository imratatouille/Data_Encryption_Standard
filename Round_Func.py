from Generate_keys_Func import generate_subkeys
from Sbox_Func import s_box
from Permutation_Func import Permutation

def Round(L_bits, R_bits, subkey):
    Left_bits = L_bits
    Right_bits = R_bits

    Clone_Right_Bits = R_bits[:]
   
    while len(Clone_Right_Bits) < 48:
        Clone_Right_Bits.append(0)   
    
    # key = "thisis64"
    # bin_key = string_to_binary(key)

    # if len(bin_key) == 64:
    #     pass
    # elif len(bin_key) < 64:
    #     while len(bin_key) < 64:
    #         bin_key.append(0)

    # subkey = generate_subkeys(bin_key)    

    XOR_Right_Key = [a ^ b for a, b in zip(Clone_Right_Bits, subkey)]

    sub_lists = [XOR_Right_Key[i:i+6] for i in range(0, len(XOR_Right_Key), 6)]

    s_box_result = []

    for i in range(8):
        s_box_result += s_box(sub_lists[i], i)
        
    s_box_result = [int(x) for x in s_box_result]

    Permutation_result = Permutation(s_box_result)

    XOR_Left_Key = [a ^ b for a, b in zip(Left_bits, Permutation_result)]

    #new right bits 수정 해야됨
    new_Left_Bits = Right_bits
    new_Right_Bits = XOR_Left_Key
    
    return new_Left_Bits, new_Right_Bits