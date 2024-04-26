from .Permutation_Func import initial_permutation, inverse_permutation
from .Round_Func import round_Func
from .Generate_keys_Func import generate_subkeys
from .String_To_Binary_Func import string_to_binary

def decryption(CT, KEY):
    key_change_to_bin = string_to_binary(f"{KEY}")
    subkeys = generate_subkeys(key=key_change_to_bin)
    clone_CT = CT[:]
    
    if len(clone_CT) < 64:
        for i in range(len(clone_CT)):
            clone_CT.extend(clone_CT[i])
            
    if len(clone_CT) > 64:
        IP_Byte = []
        for i in range(len(CT)):
            IP_Cb = initial_permutation(CT[i])
            
            Left_Cb = IP_Cb[:32]
            Right_Cb = IP_Cb[32:]
            
            for j in range(16):
                Left_Cb, Right_Cb = round_Func(Right_Cb, Left_Cb, subkeys[15-j])

            Byte = Left_Cb + Right_Cb

            IP_Byte.extend(inverse_permutation(Byte))
    else:
        IP_Cb = initial_permutation(CT)
        
        Left_Cb = IP_Cb[:32]
        Right_Cb = IP_Cb[32:]
        
        for i in range(16):
            Left_Cb, Right_Cb = round_Func(Right_Cb, Left_Cb, subkeys[15-i])

        Byte = Left_Cb + Right_Cb

        IP_Byte = inverse_permutation(Byte)
    
    return IP_Byte