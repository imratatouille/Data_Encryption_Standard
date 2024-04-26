from DES_Functions.Encryption_Func import encryption
from DES_Functions.Decryption_Func import decryption
from DES_Functions.Binary_To_Text_Func import binary_to_text_ascii, binary_to_text_utf16

PT = input("write anything: ")
KEY = input("write Key(64 bit = 8 letters): ")
Input_Text_To_binary, Encrypt_Text = encryption(PT=PT, KEY=KEY)
Decrypt_Text = decryption(CT=Encrypt_Text, KEY=KEY)


print(f"""
binary PT => {Input_Text_To_binary}
ASCII  PT => {binary_to_text_ascii(Input_Text_To_binary)}

binary CT => {Encrypt_Text}
ASCII  CT => {binary_to_text_ascii(Encrypt_Text)}
UTF-16 CT => {binary_to_text_utf16(Encrypt_Text)}

binary Decrypt CT => {Decrypt_Text}
ASCII  Decrypt CT => {binary_to_text_ascii(Decrypt_Text)}""")
