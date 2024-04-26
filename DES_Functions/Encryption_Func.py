from .String_To_Binary_Func import string_to_binary
from .Generate_keys_Func import generate_subkeys
from .Round_Func import round_Func
from .Permutation_Func import initial_permutation, inverse_permutation
from .Check_Block_Size_Func import check_block_size_func

def encryption(PT, KEY):
    key_change_to_bin = string_to_binary(f"{KEY}")
    subkeys = generate_subkeys(key=key_change_to_bin)
    
    bin_result_PT = string_to_binary(PT)
    bin_result_PT_len = len(bin_result_PT)
    
    block, block_size = check_block_size_func(bin_result_PT_len=bin_result_PT_len,bin_result_PT=bin_result_PT)
    
    all_ciper_binary = []
    
    if block_size > 1:
        for i in range(block_size):
            initial_permutated_PT = initial_permutation(block[i])
            Left_bits = initial_permutated_PT[:32]
            Right_bits = initial_permutated_PT[32:]
            for j in range(16):
                Left_bits, Right_bits = round_Func(Right_bits, Left_bits, subkeys[j])

            merge_bits = Left_bits + Right_bits
            
            all_ciper_binary.append(inverse_permutation(merge_bits))
    else:
        initial_permutated_PT = initial_permutation(block[0])

        Left_bits = initial_permutated_PT[:32]
        Right_bits = initial_permutated_PT[32:]

        for i in range(16):
            Left_bits, Right_bits = round_Func(Right_bits, Left_bits, subkeys[i])
            
        merge_bits = Left_bits + Right_bits
        
        all_ciper_binary.extend(merge_bits)
        all_ciper_binary = inverse_permutation(all_ciper_binary)
    
    
    if len(bin_result_PT) % 64 != 0:
        while len(bin_result_PT) % 64 != 0:
            bin_result_PT.append(0)

    return bin_result_PT, all_ciper_binary
