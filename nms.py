import base64
from Crypto.Cipher import AES
import json
import os
import sys

def decrypt_aes_ecb_128(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.rstrip()

def convert_value(value):
    if isinstance(value, str):
        return value.replace("\r\n", "\\r\\n").replace("\n", "\\n")
    else:
        return value

def flatten_dict(dictionary, parent_key='', separator=': '):
    items = []
    for key, value in dictionary.items():
        new_key = f"{parent_key} {key}".strip()
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, separator=separator).items())
        else:
            items.append((new_key, convert_value(value)))
    return dict(items)

def format_nested_keys(data, indent=0):
    formatted_text = ""
    for key, value in data.items():
        if isinstance(value, dict):
            formatted_text += "" * indent + f"│[۞] {key} Values\n"
            formatted_text += format_nested_keys(value, indent + 1)
        elif isinstance(value, list):
            formatted_text += "" * indent + f"│[۞] {key} Values\n"
            for item in value:
                if isinstance(item, dict):
                    formatted_text += format_nested_keys(item, indent + 1)
                elif item != 0 and item != "" and item not in [True, False]:
                    formatted_text += "" * (indent + 1) + f"{convert_value(item)}\n"
        elif value != 0 and value != "" and value not in [True, False]:
            formatted_text += "" * indent + f"│[۞] {key}: {convert_value(value)}\n"
    return formatted_text

def process_nm_content(encrypted_content, filename, print_messages=True):
    if print_messages:
        result = f""
    else:
        result = ""

    result += "┌───────────────\n│𝗦𝗣 - 𝗗𝗘𝗖𝗢𝗗𝗘 (.nm)\n│𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 : https://bit.ly/jhkhw\n├───────────────\n"

    base64_key = "X25ldHN5bmFfbmV0bW9kXw=="
    key = base64.b64decode(base64_key)

    ciphertext = base64.b64decode(encrypted_content)

    decrypted_text = decrypt_aes_ecb_128(ciphertext, key)

    formatted_text = decrypted_text.decode('utf-8')
    start_index = formatted_text.find("{")
    end_index = formatted_text.rfind("}")

    if start_index == -1 or end_index == -1 or end_index < start_index:
        if print_messages:
            print("Error: Could not find a valid JSON format.")
        return

    json_text = formatted_text[start_index:end_index + 1]

    try:
        data = json.loads(json_text)
        flattened_dict = flatten_dict(data)
        formatted_text = format_nested_keys(flattened_dict)
    except json.JSONDecodeError as e:
        if print_messages:
            print(f"Error loading JSON: {e}")
        return

    result += formatted_text
    result += "├───────────────\n│[۞] 𝗚𝗥𝗢𝗨𝗣 : @DecryptSP \n│[۞] 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 : @TEAM_CHICO_CP\n└───────────────\n"

    if print_messages:
        print(result)

def process_files_in_directory(directory, print_messages=True):
    for filename in os.listdir(directory):
        if filename.endswith(".nm"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'rb') as file:
                encrypted_text = file.read()
                process_nm_content(encrypted_text, filename, print_messages)

def main():
    if len(sys.argv) == 1:
        print("Usage: python nm.py filename.nm or python nm.py directory_path")
        return

    target_path = sys.argv[1]

    if os.path.isfile(target_path):
        with open(target_path, 'rb') as file:
            encrypted_text = file.read()
            process_nm_content(encrypted_text, target_path)
    elif os.path.isdir(target_path):
        process_files_in_directory(target_path)
    else:
        print(f"Path not found '{target_path}'")

if __name__ == "__main__":
    main()