import os
import subprocess
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import re
import random
from base64 import b64decode
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import unpad
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import json
from Crypto.Cipher import AES
import base64
import re
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram.utils.helpers import mention_html
import random
import json
import requests
import time

TOKEN = "6551770885:AAHg6I63uyKKvltalDHDr7yR-YVbaA4xu_M"  # Definición del TOKEN

extension_to_script = {
    "hat": "modulhat.js",
    "xscks": "xscks.py", 
    "phc": "phc.py", 
    "ehil": "chicosp.js",
    "mina": "mina.py",
    "nm": "nms.py",
    "tnl": "tnl.py",
    "ziv": "ziv.py",
    "pb": "pb.py", 
    "rez": "rez.js",
    "sks": "sks.js",
    "stk": "stk.js",
    "pcx": "pcx.py",
    "ssh": "ssh.py",
    "agn": "tnl2.py",
    "nt": "nt.py",
    "vpnlite": "vpnlite.py",
    "sut": "sut.py", 
    "maya": "maya.py", 
    "Fɴ": "multides.py",
    "mij": "mij.py",
    "mtl": "mtl.py",
    "fnnetwork": "fnnetwork.py", 
    "mrc": "mrc.py",
    "sksrv": "sksrv.py", 
    "sksrv.png": "sksrv.py", 
    "v2i": "multides.py", 
    "ost": "multides.py", 
    "agn": "multides.py", 
    "jvi": "multides.py", 
    "jvc": "multides.py",
    "aro": "aro.py",
    "cloudy": "cloudy.py",
    "ePro": "modulepro.js",
    "cly": "multides.py",
    "xtp": "xtproy.py",
    "roy": "xtproy.py", 
    "ipt": "ipt.py" 
}

FILES_DIR = "Downloads"

grupos_permitidos_ids = [-1002068726651, -1001685717676, -1001509659919, -1001810320865]
chat_privado_especial_id = 5325631223

def process_received_file(update: Update, context: CallbackContext):
    if update.message is None:
        print("El update no contiene un mensaje.")
        return
    
    grupo_id = update.message.chat_id
    file_info = context.bot.get_file(update.message.document.file_id)
    file_extension = file_info.file_path.split(".")[-1]
    file_name = update.message.document.file_name
    
    if grupo_id in grupos_permitidos_ids or grupo_id == chat_privado_especial_id:
        if file_extension in extension_to_script:
            downloaded_file = file_info.download_as_bytearray()
            received_file_path = os.path.join(FILES_DIR, file_name)
            with open(received_file_path, "wb") as received_file:
                received_file.write(downloaded_file)
            
            # Agregar aquí la reacción aleatoria
            emoji = random.choice(reactions)
            send_message_react(grupo_id, update.message.message_id, emoji)
                                           
            script_name = extension_to_script[file_extension]
            script_path = os.path.join(os.path.dirname(__file__), script_name)
            if file_extension in ["rez", "sks", "stk", "hat", "ePro", "ehil"]:
                script_command = f'node "{script_path}" "{received_file_path}"'
            else:
                script_command = f'python "{script_path}" "{received_file_path}"'
            
            result = subprocess.run(script_command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if result.stdout.strip():
                message_limit = 4096
                message_parts = [result.stdout[i:i+message_limit] for i in range(0, len(result.stdout), message_limit)]
                for part in message_parts:
                    update.message.reply_text(part, reply_to_message_id=update.message.message_id)
            elif result.stderr.strip():
                update.message.reply_text(f"Error: {result.stderr}", reply_to_message_id=update.message.message_id)
        else:
            pass
    else:
        access_denied_message = (
            "•‼️Access Denied‼️•\n"
            "==============================\n"
            " Contact the Developer, gain access to the Bot ✓\n\n"
            " • @CHICO_CP | • @BOSS\n\n"
            "⫹⫺ 2024 𝖠𝗅𝗅 𝗋𝗂𝗀𝗁𝗍 𝗋𝖾𝗌𝖾𝗋𝗏𝖾𝖽 | CHICO_CP ®\n"
            "=============================="
        )
        if grupo_id == chat_privado_especial_id:
            # Realizar la función especial aquí para el chat privado especial
            # Por ejemplo:
            # context.bot.send_message(chat_id=grupo_id, text="Función especial ejecutada")
            pass
        else:
            context.bot.send_message(chat_id=grupo_id, text=access_denied_message)

def is_group_allowed(grupo_id):
    if grupo_id in grupos_permitidos_ids:
        return True
    else:
        return False
#vemss://
def decodificar_base64(data):
    try:
        decoded_data = base64.b64decode(data)
        return decoded_data.decode('utf-8')
    except Exception as e:
         print("Decoded data:", decoded_data)
         return str(e)


def decodificar_vmess(update, context):
    message = update.message
    if message is not None and "vmess://" in message.text:
        start_index = message.text.find("vmess://")
        encoded_data = message.text[start_index + len("vmess://"):]
        decoded_data = decodificar_base64(encoded_data)
        configdict = json.loads(decoded_data)
        json_formatted = "│[۞] JSON:\n" + "```" + json.dumps(configdict, indent=4) + "```"
        mensaje_final = ("┌───────────────\n"
                         "│𝗦𝗣 - 𝗗𝗘𝗖𝗢𝗗𝗘 (vmess://)\n"
                         "│𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 : https://bit.ly/jhkhw\n"
                         "├───────────────\n"
                         f"{json_formatted}\n"
                         "├───────────────\n"
                         "│[۞] 𝗚𝗥𝗢𝗨𝗣 : @DecryptSP \n"
                         "│[۞] 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 : @TEAM_CHICO_CP\n"
                         "└───────────────\n")
        context.bot.send_message(chat_id=message.chat_id, text=mensaje_final, parse_mode='Markdown')
        
        
#NM-?? 
# Definir la función para eliminar caracteres aleatorios
def remove_random_characters(text):
    replacements = {
        ',': '\n',
        '"': '',
        '{': '',
        '}': '',
        'ps:': 'ProfileName: ',
        '\\': '', 
        ':': ' : '
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

# Definir la función para agregar marcadores a las líneas
def add_marker_to_lines(text, marker="│[۞] JSON: ```"):
    lines = text.split('\n')
    marked_lines = [f'{marker} {line}```' for line in lines]
    marked_text = '\n'.join(marked_lines)
    return marked_text

# Definir la función principal para manejar los mensajes
def decrypted_config(update, context):
    message = update.message

    # Verificar si el mensaje proviene de un chat privado
    if message.chat.type == 'private':
        context.bot.send_message(message.chat.id, "•‼️Access Denied‼️•\n==============================\n Contact the Developer, gain access to the Bot ✓\n\n • @CHICO_CP | • @Nextdec\n\n⫹⫺  2024 𝖠𝗅𝗅 𝗋𝗂𝗀𝗁𝗍 𝗋𝖾𝗌𝖾𝗋𝗏𝖾𝖽 | CHICO_CP ®\n==============================")
        return

    encrypted_text_base64 = message.text.strip()

    # Verificar si el mensaje coincide con el patrón esperado
    pattern = r'^nm-(dns|vless|vmess|trojan|ssr)://'
    cfg_type = re.match(pattern, encrypted_text_base64)

    if cfg_type is None:
        # Si el mensaje no coincide con el patrón, no hacer nada
        return

    try:
        cle = 'X25ldHN5bmFfbmV0bW9kXw=='  # Clave de cifrado base64
        encryption_key = base64.b64decode(cle)

        # Extraer y decodificar el texto cifrado
        config_encrypt = encrypted_text_base64[len(cfg_type[0]):]
        encrypted_text = base64.b64decode(config_encrypt)

        cipher = AES.new(encryption_key, AES.MODE_ECB)
        decrypt_text = unpad(cipher.decrypt(encrypted_text), AES.block_size)

        # Decodificar el texto
        decrypt_text = decrypt_text.decode('utf-8')

        # Crear el mensaje formateado
        formatted_text = add_marker_to_lines(remove_random_characters(decrypt_text))
        mensaje_final = (
            "┌───────────────\n"
            "│𝗦𝗣 - 𝗗𝗘𝗖𝗢𝗗𝗘 (NET MOD SYNA)\n"
            "│𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 : https://bit.ly/jhkhw\n"
            "├───────────────\n"
            f"{formatted_text}\n"
            "├───────────────\n"
            "│[۞] 𝗚𝗥𝗢𝗨𝗣 : @DecryptSP \n"
            "│[۞] 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 : @TEAM_CHICO_CP\n"
            "└───────────────\n"
        )

        context.bot.send_message(chat_id=message.chat_id, text=mensaje_final, parse_mode='Markdown')
    except Exception as e:
        context.bot.send_message(chat_id=message.chat_id, text=f"Error decoding message: {str(e)}")
        
def is_user_in_channel(bot, user_id, channel_id):
    try:
        member = bot.get_chat_member(channel_id, user_id)
        return True if member.status != "left" else False
    except Exception as e:
        print(f"Error checking user membership: {e}")
        return False     

def is_user_subscribed_to_both_channels(bot, user_id, channels):
    try:
        for channel_id in channels:
            member = bot.get_chat_member(channel_id, user_id)
            if member.status == "left":
                return False
        return True
    except Exception as e:
        print(f"Error checking user subscription: {e}")
        return False                          

def start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    chat_type = update.message.chat.type
    channels = [-1001602342237]  # Lista de canales requeridos
    
    if chat_type == 'private' or chat_type in ['group', 'supergroup']:
        # Comprobar si el usuario está en los canales requeridos
        for channel_id in channels:
            if not is_user_in_channel(context.bot, user_id, channel_id):
                context.bot.send_message(update.message.chat_id, f"Please join our channel: https://t.me/TEAM_CHICO_CP")
                return
        
        # Enviar mensaje de bienvenida
        send_welcome_message(update.message)

def send_welcome_message(message):
    user = message.from_user
    last_name = message.from_user.full_name
    username = user.username
    user_id = message.chat_id
    group_link = f"https://t.me/DecryptSP"
    
    photos = message.bot.get_user_profile_photos(user_id).photos
    photo_file_id = None
    
    try:
        if photos:
            photo_file_id = photos[0][-1].file_id
            message.bot.send_photo(
                message.chat_id,
                photo=photo_file_id,
                caption=f"""⚕ 𓆰 Welcome {last_name}
-  -  -  ‌-  -  -  ‌-  -  -  ‌
• 🤍 | User: @{username}
• 🍷 | Link: https://t.me/{username}
• 🐊 | ID: {user_id}
• 🦇 | Name: {last_name} 
• 🌐 | Group Link: {group_link}
-  -  -  ‌-  -  -  ‌-  -  -  ‌
🍷Developer: - @CHICO_CP
👑 Owner: - @CHICO_CP"""
            )
        else:
            message.bot.send_message(
                message.chat_id,
                text=f"""⚕ 𓆰 Welcome {last_name}
-  -  -  ‌-  -  -  ‌-  -  -  ‌
• 🤍 | User: @{username}
• 🍷 | Link: https://t.me/{username}
• 🐊 | ID: {user_id}
• 🦇 | Name: {last_name} 
• 🌐 | Group Link: {group_link}
-  -  -  ‌-  -  -  ‌-  -  -  ‌
🍷Developer: - @CHICO_CP
👑 Owner: - @CHICO_CP"""
            )
    except AttributeError:
        message.bot.send_message(
            message.chat_id,
            text=f"""⚕ 𓆰 Welcome {last_name}
-  -  -  ‌-  -  -  ‌-  -  -  ‌
• 🤍 | User: @{username}
• 🍷 | Link: https://t.me/{username}
• 🐊 | ID: {user_id}
• 🦇 | Name: {last_name} 
• 🌐 | Group Link: {group_link}
-  -  -  ‌-  -  -  ‌-  -  -  ‌
🍷Developer: - @CHICO_CP
👑 Owner: - @CHICO_CP"""
        )

def send_welcome_message_group(bot, message):
    bot.send_message(
        message.chat_id,
        f"""⚕ 𓆰 Welcome to our group! Feel free to explore and engage with other members. If you have any questions, don't hesitate to ask."""
    )
#Welcome
def welcome_new_member(update: Update, context: CallbackContext):
    # Obtener la información sobre el nuevo miembro
    new_members = update.message.new_chat_members

    for new_member in new_members:
        # Obtener el nombre de usuario o nombre del nuevo miembro
        new_member_name = new_member.username or new_member.first_name

        # Crear el mensaje de bienvenida con el mismo texto que el comando /start
        welcome_message = (f"⚕ 𓆰 Welcome {new_member_name}\n"
                           " -  -  -  ‌-  -  -  ‌-  -  -  ‌\n"
                           "• 🤍 | User: @{new_member_name}\n"
                           f"• 🍷 | Link: https://t.me/{new_member_name}\n"
                           f"• 🐊 | ID: {new_member.id}\n"
                           f"• 🦇 | Name: {new_member_name}\n"
                           f"• 🌐 | Group Link: https://t.me/DecryptSP\n"
                           " -  -  -  ‌-  -  -  ‌-  -  -  ‌\n"
                           "🍷Developer: - @CHICO_CP\n"
                           "👑 Owner: - @CHICO_CP")

        # Obtener la foto de perfil del nuevo miembro si está disponible
        photo_file_id = new_member.get_profile_photos().photos[-1][-1].file_id if new_member.get_profile_photos().photos else None

        # Enviar el mensaje de bienvenida al grupo
        if photo_file_id:
            context.bot.send_photo(update.message.chat_id, photo=photo_file_id, caption=welcome_message, parse_mode='Markdown')
        else:
            update.message.reply_text(welcome_message, parse_mode='Markdown')   

# Función para manejar mensajes howdy://

def cbc_iv(data):
    data = data.replace("\n", "")
    cipher = AES.new(b'poiuytrewqas+=~|', AES.MODE_CBC, b'r4tgv3b2zcmdW6ZZ')
    decrypted_data = cipher.decrypt(base64.b64decode(data))
    return decrypted_data.decode()
    
def handle_message(update, context):
    message = update.message
    chat_id = message.chat.id
    text = message.text
    message_id = message.message_id

    try:
        decode = text.split('://')[1]
        data = base64.b64decode(decode)
        json_data = json.loads(data)
        username = json_data['username']
        password = json_data['password']
        port = json_data['port']
        server = json_data['server']
        dataa = cbc_iv(server)
        sni = json_data['sni']
        sni2 = cbc_iv(sni)
        type = json_data['type']
        linkserver = f"│[۞] Username: {username}\n│[۞] Password: {password}\n│[۞] Server: {dataa}\n│[۞] Port: {port}\n│[۞] Type: {type}"
        context.bot.send_message(chat_id, f"<strong>┌───────────────\n│𝗦𝗣 - 𝗗𝗘𝗖𝗢𝗗𝗘 (howdy://)\n│𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 : https://bit.ly/jhkhw\n├───────────────\n{linkserver}\n├───────────────\n│[۞] 𝗚𝗥𝗢𝗨𝗣 : @DecryptSP \n│[۞] 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 : @TEAM_CHICO_CP\n├───────────────\n│[۞] Developer : @PhoenixMY\n└─────────────── </strong>", parse_mode="html", reply_to_message_id=message_id)
    except Exception as e:
        context.bot.send_message(chat_id, f"Oops, there was an error, bro: {str(e)}", reply_to_message_id=message_id)
                    
#Armod vpn
# Asegúrate de que estas funciones están definidas en tu código
def add_marker_to_lines(text):
    # Implementación de esta función
    pass

def add_second_marker_to_lines(text, protocol):
    # Implementación de esta función
    pass
def armod(update, context):
    message = update.message
    encrypted_text_base64 = message.text.strip()
    cle = 'YXJ0dW5uZWw3ODc5Nzg5eA==' 
    pattern = r'^ar-(dns|vless|vmess|trojan|ssr|socks|trojan-go|ssh)://'
    cfg_type = re.match(pattern, encrypted_text_base64)
    try:
        if cfg_type is not None:
            encryption_key = base64.b64decode(cle)

            config_encrypt = encrypted_text_base64[len(cfg_type[0]):]
            encrypted_text = base64.b64decode(config_encrypt)

            # Desencriptar texto
            cipher = AES.new(encryption_key, AES.MODE_ECB)
            decrypt_text = unpad(cipher.decrypt(encrypted_text), AES.block_size)
            decrypt_text = decrypt_text.decode('utf-8')
            
            # Formatear texto con marcadores
            formatted_text = add_marker_to_lines(decrypt_text)
            formatted_text2 = add_marker_to_lines(decrypt_text, cfg_type[1])
            
            # Información adicional
            final_text = ("┌───────────────\n│𝗦𝗣 - 𝗗𝗘𝗖𝗢𝗗𝗘 (ar-??)\n│𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 : https://bit.ly/jhkhw\n├───────────────\n"
                          f"{formatted_text}\n{formatted_text2}\n"
                          "├───────────────\n│[۞] 𝗚𝗥𝗢𝗨𝗣 : @DecryptSP \n│[۞] 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 : @TEAM_CHICO_CP\n├───────────────\n└─────────────── ")
            
            # Enviar el texto final al chat
            context.bot.send_message(chat_id=message.chat.id, text=final_text, reply_to_message_id=message.message_id, parse_mode='Markdown')
        else:
            context.bot.send_message(chat_id=message.chat.id, text="Formato no reconocido. Asegúrese de usar un formato compatible.", reply_to_message_id=message.message_id)
    except Exception as e:
        print(f"Error: {e}")
        context.bot.send_message(chat_id=message.chat.id, text=f"Lo siento, hubo un error al decodificar: {str(e)}", reply_to_message_id=message.message_id)
        
 # Lista de reacciones
reactions = ["❤️", "😍", "😐", "💋", "🥰", "😁", "👍", "👎", "🔥", "👏", "🤔", "🤯", "😱", "🤬", "🥲", "❤️‍🔥", 
             "💔", "🌚", "🌭", "💯", "🤣", "🍌", "🤩", "🤮", "💩", "🙏", "👌", "🕊️", "🤡", "🥱", "🥴", "🐳", 
             "🏆", "🤨", "🍓", "🖕", "😈", "😴", "😭", "🤓", "👻", "⚡️", "👀", "🙈", "😇", "😨", "🤝", "✍️", 
             "🤗", "🫡", "👨‍💻", "🤷", "🤷‍♂", "🤷‍♀", "😡", "😎", "🙊", "👾", "🎄", "💊️"]

def send_message_react(chat_id, message_id, emoji):
    url = f"https://api.telegram.org/bot{TOKEN}/setmessagereaction"
    data = {
        'chat_id': chat_id,
        'message_id': message_id,
        'reaction': json.dumps([{'type': "emoji", "emoji": emoji}])
    }
    response = requests.post(url, data=data)
    if response.status_code != 200:
        return f"Error: {response.text}"
    else:
        return response.json()

def handle_message(update, context):
    message = update.message
    if message is None:
        # Registra el error o manéjalo según sea necesario
        print("Recibido update sin mensaje.")
        return

    chat_id = message.chat_id
    message_id = message.message_id
    
    # Verificar si el mensaje fue enviado por un usuario anónimo
    if message.from_user is None:
        # Seleccionar una reacción aleatoria
        emoji = random.choice(reactions)
        
        # Enviar la reacción
        response = send_message_react(chat_id, message_id, emoji)
    else:
        # Verificar si el mensaje contiene un documento o texto
        if message.document or message.text:
            # Seleccionar una reacción aleatoria
            emoji = random.choice(reactions)
            
            # Enviar la reacción
            response = send_message_react(chat_id, message_id, emoji)
       
#Start
def main():
    try:
        os.makedirs(FILES_DIR, exist_ok=True)
        updater = Updater(TOKEN, use_context=True)
        dispatcher = updater.dispatcher
        dp = updater.dispatcher

        # Manejador para el comando '/start'
        start_handler = CommandHandler('start', start)
        dispatcher.add_handler(start_handler)

        # Manejador para archivos recibidos
        file_handler = MessageHandler(Filters.document, process_received_file)
        dispatcher.add_handler(file_handler)

        # Manejador para mensajes
        dp.add_handler(MessageHandler(Filters.all, handle_message))

        # Manejador para dar la bienvenida a nuevos miembros
        welcome_handler = MessageHandler(Filters.status_update.new_chat_members, welcome_new_member)
        dispatcher.add_handler(welcome_handler)

        print("Bot activo. Esperando mensajes...")

        updater.start_polling()

        updater.idle()

    except Exception as e:
        logging.error(f"Ocurrió una excepción: {str(e)}")

if __name__ == '__main__':
    main()