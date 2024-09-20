from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import hashlib
import sys

def decrypt_aes_cbc_pkcs7(ciphertext, key):
    hashed_key = hashlib.sha256(key.encode()).digest()
    ciphertext = base64.b64decode(ciphertext)
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    cipher = AES.new(hashed_key, AES.MODE_CBC, iv)  
      
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    return plaintext.decode('utf-8')
def print_config(config_str):
    config_data = config_str.strip().strip('{}').split(',')    
    config_list = [item.split(':') for item in config_data]
        
    for pair in config_list:
        if len(pair) >= 2:  
            key = pair[0].strip('"')
            value = pair[1].strip('"')
            print(f"│[۞] {key}: {value}")
def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py <archivo_encriptado>")
        return    
    file_path = sys.argv[1]    
    with open(file_path, 'rb') as file:
        ciphertext = file.read()    
    key = "Wasjdeijs@/ÇPãoOf231#$%¨&*()_qqu&iJo>ç"
        
    plaintext = decrypt_aes_cbc_pkcs7(ciphertext, key)
    print("┌───────────────\n│𝗦𝗣 - 𝗗𝗘𝗖𝗢𝗗𝗘 (.vpnlite)\n│𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 : https://bit.ly/jhkhw\n├───────────────")
    print_config(plaintext)
    print("├───────────────\n│[۞] 𝗚𝗥𝗢𝗨𝗣 : @DecryptSP \n│[۞] 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 : @TEAM_CHICO_CP\n│[۞] 𝗢𝗪𝗡𝗘𝗥: @CHICO_CP\n└───────────────\n") 

if __name__ == "__main__":
    main()