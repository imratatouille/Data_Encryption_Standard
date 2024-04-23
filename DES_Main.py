from Initial_Permutation_Func import initial_permutation
from String_To_binary_Func import string_to_binary
from Generate_keys_Func import generate_subkeys
from Sbox_Func import s_box
from Permutation_Func import Permutation

# 문자열 받기
CT = input("아무거나 적어주세요: ")

# 평문을 이진수로 변환하기 & 리스트 안에 들어간 이진값의 갯수
bin_result_CT = string_to_binary(CT)
bin_result_CT_len = len(bin_result_CT)

# 리스트 안에 들어있는 이진값의 갯수를 64비트로 만드는 조건문
bin_list = []
if bin_result_CT_len == 64:
    pass
elif bin_result_CT_len > 64:
    for i in range(0, len(bin_result_CT), 64):
        bin_list = bin_result_CT[i:i+64]
        bin_list.extend([0] * (64 - len(bin_result_CT)))
        bin_list.append(bin_list)
elif bin_result_CT_len < 64:
    while len(bin_result_CT) < 64:
        bin_result_CT.append(0)
    
# initial permution 된 평문
initial_permutated_CT = initial_permutation(bin_result_CT)

# initial permution 된 평문을 32비트씩 나누기
Left_bits = initial_permutated_CT[:32]
Right_bits = initial_permutated_CT[32:]

Clone_Right_Bits = initial_permutated_CT[:32]
Clone_Left_Bits = Left_bits

while len(Clone_Right_Bits) < 48:
    Clone_Right_Bits.append(0)
    
key = ""
bin_key = string_to_binary(key)

if len(bin_key) == 64:
    pass
elif len(bin_key) < 64:
    while len(bin_key) < 64:
        bin_key.append(0)

subkey = generate_subkeys(bin_key)    

XOR_Right_Key = [a ^ b for a, b in zip(Clone_Right_Bits, subkey[0])]

sub_lists = [XOR_Right_Key[i:i+6] for i in range(0, len(XOR_Right_Key), 6)]

s_box_result = []

for i in range(8):
    s_box_result += s_box(sub_lists[i], i)
    
s_box_result = [int(x) for x in s_box_result]

Permutation_result = Permutation(s_box_result)

XOR_Left_Key = [a ^ b for a, b in zip(Clone_Left_Bits, Permutation_result)]

#new right bits 수정 해야됨
new_Left_Bits = Right_bits
new_Right_Bits = XOR_Left_Key

print(len(new_Left_Bits),len(new_Right_Bits))