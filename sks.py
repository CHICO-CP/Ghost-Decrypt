import sys
import os
import json
from Crypto.Cipher import AES
import base64 
from Crypto.Hash import MD5

if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]):
    print("[ERROR] Ruta no especificada o archivo inexistente")
    sys.exit(1)

file = sys.argv[1]

if os.path.splitext(file)[1] != ".sks":
    sys.exit()

try:
    with open(sys.argv[1], "r") as f:
        configFile = json.loads(f.read())
except Exception as e:
    print("[ERROR] Datos JSON inválidos:", e)
    sys.exit()

configKeys = [
    "662ede816988e58fb6d057d9d85605e0",
    "162exe235948e37ws6d057d9d85324e2",
    "962exe865948e37ws6d057d4d85604e0",
    "175exe868648e37wb9x157d4l45604l0",
    "175exe867948e37wb9d057d4k45604l0",
]

def aesDecrypt(data, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(data)
    return decrypted.decode('utf-8').rstrip('\0')

def md5crypt(data):
    h = MD5.new()
    h.update(data)
    return h.hexdigest()

def parseConfig(data):
    print('┌───────────────\n│ 𝗗𝗘𝗖𝗥𝗬𝗣𝗧 𝗠𝗨𝗟𝗧𝗜𝗣𝗟𝗘 ({})\n│𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 : https://bit.ly/jhkhw\n├───────────────'.format(os.path.splitext(file)[1]))
    print(f"│[۞] SSH Server: {data['sshServer']}")
    print(f"│[۞] SSH Port: {data['sshPort']}")
    print(f"│[۞] SSH Username: {data['profileSshAuth']['sshUser']}")
    
    if 'sshPasswd' in data['profileSshAuth']:
        print(f"│[۞] SSH Password: {data['profileSshAuth']['sshPasswd']}")
    
    if 'sshPublicKey' in data['profileSshAuth']:
        print(f"│[۞] SSH PublicKey:\n{data['profileSshAuth']['sshPublicKey']}")
    
    if 'enableDataCompression' in data:
        print(f"│[۞] Enable Data Compress: {data['enableDataCompression']}")
    
    if 'disableTcpDelay' in data:
        print(f"│[۞] Disable TCP Delay: {data['disableTcpDelay']}")
    
    if 'proxyType' in data:
        print(f"│[۞] Tunnel type: {'SSH + HTTP' if data['proxyType'] == 'PROXY_HTTP' else 'SSH + SSL/TLS' if data['proxyType'] == 'PROXY_SSL' else 'Undefined'}")
    else:
        print(f"│[۞] Tunnel Type: SSH DIRECT")
    
    if 'proxyHttp' in data:
        if 'proxyIp' in data['proxyHttp']:
            print(f"│[۞] Proxy Host: {data['proxyHttp']['proxyIp']}")
        if 'proxyPort' in data['proxyHttp']:
            print(f"│[۞] Proxy Port: {data['proxyHttp']['proxyPort']}")
        if 'isCustomPayload' in data['proxyHttp']:
            print(f"│[۞] Use Custom Payload Proxy: {data['proxyHttp']['isCustomPayload']}")
        if 'customPayload' in data['proxyHttp']:
            print(f"│[۞] Proxy Payload:\n{data['proxyHttp']['customPayload']}")
    
    if 'proxySsl' in data:
        if 'hostSni' in data['proxySsl']:
            print(f"│[۞] SNI Value: {data['proxySsl']['hostSni']}")
        if 'versionSSl' in data['proxySsl']:
            print(f"│[۞] SSL Version: {data['proxySsl']['versionSSl']}")
        if 'isSSLCustomPayload' in data['proxySsl']:
            print(f"│[۞] Use Custom Payload SSL: {data['proxySsl']['isSSLCustomPayload']}")
        if 'customPayloadSSL' in data['proxySsl']:
            print(f"│[۞] SSL Payload:\n{data['proxySsl']['customPayloadSSL']}")
    
    if 'proxyDirect' in data:
        if 'isCustomPayload' in data['proxyDirect']:
            print(f"│[۞] Use Custom Payload: {data['proxyDirect']['isCustomPayload']}")
        if 'customPayload' in data['proxyDirect']:
            print(f"│[۞] Payload: {data['proxyDirect']['customPayload']}")
    
    if 'dnsCustom' in data:
        print(f"│[۞] Custom DNS Servers: {json.dumps(data['dnsCustom'])}")
    
    if 'isUdpgwForward' in data:
        print(f"│[۞] Forward UDPGW: {data['isUdpgwForward']}")
    
    if 'configProtect' in data:
        if 'blockConfig' in data['configProtect']:
            print(f"│[۞] Block config: {data['configProtect']['blockConfig']}")
        if 'validity' in data['configProtect']:
            print(f"│[۞] Expire Date: {str(data['configProtect']['validity'])}")
        if 'blockRoot' in data['configProtect']:
            print(f"│[۞] Block Root: {data['configProtect']['blockRoot']}")
        if 'blockAuthEdition' in data['configProtect']:
            print(f"│[۞] Only Playstore: {data['configProtect']['blockAuthEdition']}")
        if 'onlyMobileData' in data['configProtect']:
            print(f"│[۞] Only Mobile Data: {data['configProtect']['onlyMobileData']}")
        if 'blockByPhoneId' in data['configProtect']:
            print(f"│[۞] HWID Enabled: {data['configProtect']['blockByPhoneId']}")
        if 'message' in data['configProtect']:
            print(f"│[۞] Note:\n{data['configProtect']['message']}")
        if 'phoneId' in data['configProtect']:
            print(f"│[۞] HWID Value: {data['configProtect']['phoneId']}")
        if 'hideMessageServer' in data['configProtect']:
            print(f"│[۞] Hide Server Message: {data['configProtect']['hideMessageServer']}")
        print('├───────────────\n│[۞] 𝗚𝗥𝗢𝗨𝗣 : @file_decryptors \n│[۞] 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 : @TEAM_CHICO_CP\n└───────────────\n')

try:
    decrypted_data = aesDecrypt(
        configFile['d'].split(".")[0].encode('utf-8'),
        md5crypt((configKeys[1] + " " + configFile['v']).encode('utf-8')).encode('utf-8'),
        base64.b64decode(configFile['d'].split(".")[1])
    )
    parseConfig(json.loads(decrypted_data))
except Exception as e:
    print("[ERROR] Error inesperado:", e)