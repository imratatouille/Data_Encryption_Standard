from DES_Functions.Encryption_Func import encryption
from DES_Functions.Decryption_Func import decryption
from DES_Functions.Binary_To_Text_Func import binary_to_text_ascii

PT = input("write anything: ")
# KEY = input("write Key(64 bit = 8 letters): ")
KEY = "thisis64"

Encrypt_Texts = []

Input_Text_To_binary, Encrypt_Text = encryption(PT=PT, KEY=KEY)
clone_Encrypt_Text = Encrypt_Text[:]

if len(clone_Encrypt_Text) < 64:
    for i in range(len(clone_Encrypt_Text)):
        clone_Encrypt_Text.extend(clone_Encrypt_Text[i])

if len(clone_Encrypt_Text) > 64:
    for i in range(len(Encrypt_Text)):
        Encrypt_Texts.extend(Encrypt_Text[i])
        
Decrypt_Text = decryption(CT=Encrypt_Text, KEY=KEY)


print(f"""
binary PT => {Input_Text_To_binary}
ASCII  PT => {binary_to_text_ascii(Input_Text_To_binary)}

binary CT => {Encrypt_Texts}
ASCII  CT => {binary_to_text_ascii(Encrypt_Texts)}

binary Decrypt CT => {Decrypt_Text}
ASCII  Decrypt CT => {binary_to_text_ascii(Decrypt_Text)}""")
