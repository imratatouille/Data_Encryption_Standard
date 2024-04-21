from Initial_Permutation_Func import initial_permutation
from String_To_binary_Func import string_to_binary
from Generate_keys_Func import generate_subkeys
# from Sbox_Func import s_box

# 문자열 받기
CT = input("아무거나 적어주세요: ")

# 평문을 이진수로 변환하기 & 리스트 안에 들어간 이진값의 갯수
bin_result_CT = string_to_binary(CT)
bin_result_CT_len = len(bin_result_CT)

# 리스트 안에 들어있는 이진값의 갯수를 64비트로 만드는 조건문
if bin_result_CT_len == 64:
    pass
elif bin_result_CT_len > 64:
    bin_result_CT_len[:64]
elif bin_result_CT_len < 64:
    while len(bin_result_CT) < 64:
        bin_result_CT.append(0)
    
# initial permution 된 평문
initial_permutated_CT = initial_permutation(bin_result_CT)

# initial permution 된 평문을 32비트씩 나누기
Left_bits = initial_permutated_CT[:32]
Right_bits = initial_permutated_CT[32:]

Key_Right_Bits = Right_bits

while len(Key_Right_Bits) < 48:
    Key_Right_Bits.append(0)
    
key = "dqwdqw"
bin_key = string_to_binary(key)

if len(bin_key) == 64:
    pass
elif len(bin_key) < 64:
    while len(bin_key) < 64:
        bin_key.append(0)

subkey = generate_subkeys(bin_key)    

XOR_Right_Key = [a ^ b for a, b in zip(Key_Right_Bits, subkey)]

sub_lists = [XOR_Right_Key[i:i+6] for i in range(0, len(XOR_Right_Key), 6)]

# s_box_list = []
# for i in range(1,9):
#     s_box_list += s_box(sub_lists, i)

#new right bits 수정 해야됨
new_Left_Bits = Right_bits
new_Right_Bits = Left_bits


print(Key_Right_Bits)
print(subkey)
print(XOR_Right_Key)