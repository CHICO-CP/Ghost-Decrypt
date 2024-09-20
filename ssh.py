import sys
import re
import random
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import unpad
from base64 import b64decode

unlockKeys = {
    "cproxyRemoto": "",
    "sslProxy": "",
    "dnsKey": "",
    "cchaveKey": "",
    "cserverNameKey": "",
    "cdnssshUser": "",
    "cdnssshPass": ""
}

def ssh_injector(file):
    key = b'263386285977449155626236830061505221752'
    text = b64decode(open(file, 'rb').read())
    iv = b'\x00\x01\x02\x03\x04\x05\x06\x07'
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    plaintext = cipher.decrypt(text)
    decrypt_text = unpad(plaintext, Blowfish.block_size).decode()  # remove pkcs#7

    principio_result_str = "┌───────────────\n│𝗦𝗣 - 𝗗𝗘𝗖𝗢𝗗𝗘 (.ssh)\n│𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 : https://bit.ly/jhkhw\n├───────────────\n"

    # Proceso de extracción de datos
    extracted_data = re.findall(r'<entry key="([^"]+)">([^"]+)</entry>', decrypt_text)
    
    # Lista de emojis
    emojis = ["💠", "🔵", "💀", "🤖",  "😈", "🔥", "🚀", "🔐"]

    # Elegir un emoji aleatorio
    random_emoji = random.choice(emojis)

    result_message = []

    for key, value in extracted_data:
        # Verificar si la clave está presente en unlockKeys o contiene el texto "unlockKeys"
        if key not in unlockKeys and "unlockKeys" not in key:
            # Usar el mismo emoji para todas las entradas
            result_message.append(f"│[{random_emoji}] {key} : {value}")

    # Ordenar los datos extraídos
    sorted_result = sorted(result_message, key=lambda x: x.split(':')[0].strip())

    # Manejar los datos de unlockKeys
    unlock_keys_message = [f"│[{random_emoji}] unlockKeys 🔽"]
    for key, value in unlockKeys.items():
        if value:
            unlock_keys_message.append(f"│[{random_emoji}] {key}: {value}")
        else:
            unlock_keys_message.append(f"│[{random_emoji}] {key}: ***")

    # Agregar los datos de unlockKeys debajo del encabezado correspondiente
    result_str = principio_result_str + '\n'.join(sorted_result[:6]) + '\n' + '\n'.join(unlock_keys_message) + '\n' + '\n'.join(sorted_result[6:]) + f"\n├───────────────\n│[{random_emoji}] 𝗚𝗥𝗢𝗨𝗣 : @DecryptSP \n├───────────────\n│[{random_emoji}] 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 : @TEAM_CHICO_CP\n└───────────────\n"

    return result_str

def main():
    if len(sys.argv) != 2:
        print("Uso: python ssh.py file.ssh")
        sys.exit(1)

    file_path = sys.argv[1]

    result = ssh_injector(file_path)
    print(result)

if __name__ == "__main__":
    main()