from Functions.Permutation_Func import initial_permutation, inverse_permutation
from Functions.String_To_Binary_Func import string_to_binary
from Functions.Generate_keys_Func import generate_subkeys
from Functions.Round_Func import Round
from Functions.Binary_To_Text_Func import binary_to_text

key_change_to_bin = string_to_binary("thisis64")
subkeys = generate_subkeys(key=key_change_to_bin)

Plain_Text = input("\nwrite anyting: ")

bin_result_PT = string_to_binary(Plain_Text)
bin_result_PT_len = len(bin_result_PT)

bin_list = bin_result_PT
if bin_result_PT_len == 64:
    print("\ninput bits == 64 bits")
elif bin_result_PT_len > 64:
    for i in range(0, len(bin_result_PT), 64):
        bin_chunk = bin_result_PT[i:i+64]
        bin_chunk.extend([0] * (64 - len(bin_list)))
        bin_list.append(bin_chunk)
    print("\ninput bits > 64 bits")
elif bin_result_PT_len < 64:
    while len(bin_result_PT) < 64:
        bin_list.append(0)
    print("\ninput bits < 64 bits")

initial_permutated_PT = initial_permutation(bin_list)

Left_bits = initial_permutated_PT[:32]
Right_bits = initial_permutated_PT[32:]

for i in range(16):
    Left_bits, Right_bits = Round(Left_bits, Right_bits, subkeys[i])

LplusR = Left_bits + Right_bits

Ciper_binery = inverse_permutation(LplusR)
Texts = binary_to_text(Ciper_binery)

print(f"""
cryptogram => {Texts}
encrypted binary number => {Ciper_binery}
""")