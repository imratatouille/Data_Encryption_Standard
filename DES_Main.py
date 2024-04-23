from Initial_Permutation_Func import initial_permutation, Reverse_permutation
from String_To_Binary_Func import string_to_binary
from Generate_keys_Func import generate_subkeys
from Round_Func import Round
import binascii
#subkey 생성
key_change_to_bin = string_to_binary("thisis64")
subkeys = generate_subkeys(key=key_change_to_bin)

# 문자열 받기
Plain_Text = input("아무거나 적어주세요: ")

# 평문을 이진수로 변환하기 & 리스트 안에 들어간 이진값의 갯수
bin_result_PT = string_to_binary(Plain_Text)
bin_result_PT_len = len(bin_result_PT)

# 리스트 안에 들어있는 이진값의 갯수를 64비트로 만드는 조건문
bin_list = bin_result_PT
if bin_result_PT_len == 64:
    print("비트값 == 64")
elif bin_result_PT_len > 64:
    for i in range(0, len(bin_result_PT), 64):
        bin_chunk = bin_result_PT[i:i+64]
        bin_chunk.extend([0] * (64 - len(bin_list)))
        bin_list.append(bin_chunk)
    print("비트값 > 64")
elif bin_result_PT_len < 64:
    while len(bin_result_PT) < 64:
        bin_list.append(0)
    print("비트값 < 64")

# initial permution 된 평문
initial_permutated_PT = initial_permutation(bin_list)

# initial permution 된 평문을 32비트씩 나누기

Left_bits = initial_permutated_PT[:32]
Right_bits = initial_permutated_PT[32:]

L_round1, R_round1 = Round(Left_bits, Right_bits, subkeys[0])
L_round2, R_round2 = Round(L_round1, R_round1, subkeys[1])
L_round3, R_round3 = Round(L_round2, R_round2, subkeys[2])
L_round4, R_round4 = Round(L_round3, R_round3, subkeys[3])
L_round5, R_round5 = Round(L_round4, R_round4, subkeys[4])
L_round6, R_round6 = Round(L_round5, R_round5, subkeys[5])
L_round7, R_round7 = Round(L_round6, R_round6, subkeys[6])
L_round8, R_round8 = Round(L_round7, R_round7, subkeys[7])
L_round9, R_round9 = Round(L_round8, R_round8, subkeys[8])
L_round10, R_round10 = Round(L_round9, R_round9, subkeys[9])
L_round11, R_round11 = Round(L_round10, R_round10, subkeys[10])
L_round12, R_round12 = Round(L_round11, R_round11, subkeys[11])
L_round13, R_round13 = Round(L_round12, R_round12, subkeys[12])
L_round14, R_round14 = Round(L_round13, R_round13, subkeys[13])
L_round15, R_round15 = Round(L_round14, R_round14, subkeys[14])
L_round16, R_round16 = Round(L_round15, R_round15, subkeys[15])

Plus_LR = L_round16 + R_round16

# rounds = 16
# LR_pairs = [(Left_bits, Right_bits)]
# for _ in range(rounds):
#     Left_bits, Right_bits = Round(Left_bits, Right_bits)
#     LR_pairs.append((Left_bits, Right_bits))

# L_rounds, R_rounds = zip(*LR_pairs)
# LR_round = L_rounds + R_rounds

# print(len(Plus_LR))
# print(len(LR_round[15]))
# Ciper_Text = Reverse_permutation(LR_round[15])

Ciper_Text = Reverse_permutation(Plus_LR)

decimal_number_list = []

for i in range(0, len(Ciper_Text), 8):
    byte = Ciper_Text[i:i+8]
    binary_string = ''.join(map(str, byte))
    decimal_number = int(binary_string, 2)
    decimal_number_list.append(decimal_number)
    text = bytes(decimal_number_list)
   
plaintext_bytes = text
plaintext =  binascii.b2a_base64(plaintext_bytes)

print(plaintext)

print(Ciper_Text)