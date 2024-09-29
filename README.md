# Ghost-Decrypt

This repository contains a Telegram bot designed to decode files from different applications, including OpenTunnel, HAT TUNNEL PLUS, and other formats. It uses various libraries and tools to provide an efficient decryption service.

## Features

- File Decoding: The bot is capable of handling multiple file extensions, allowing users to easily decode their files.
- **Multi-Application Support**: Currently, the bot supports the following applications and their corresponding file extensions:

  - ACE TUNNEL (.act)
  - AIO TUNNEL (.xscks)
  - AUSTRO PLUS (.aro)
  - BINKE TUNNEL (.pcx)
  - CMAC TUNNEL (.mc)
  - DAVID HTTP (.dvd)
  - EUGINE PRO (.eug)
  - FIRENET TUNNEL (.fnet)
  - HAT TUNNEL PLUS (.hat)
  - IP TUNNEL (.ipt)
  - JV CUSTOM (.jvc)
  - JV INJECTOR (.jvi)
  - MAVENX INJECTOR (.mij)
  - MAVENX TUNNEL (.mtl)
  - MAYA TUN UDP (.maya)
  - MINA PRO (.mina)
  - MR CUSTOM (.mrc)
  - NETMOD SYNA (.nm)
  - OPEN TUNNEL (.tnl)
  - OUSS TUNNEL (.ost)
  - PB INJECTOR (.pb)
  - PHC TUNNEL (.phc)
  - REZ TUNNEL (.rez)
  - REZ TUNNEL LITE (.rezl)
  - ROYAL TUNNEL (.roy)
  - SECOND VPN LITE (.vpnlite)
  - SMK TUN+ (.sut)
  - SOCKS HTTP (.sks)
  - SOCKS REVIVE (.sksrv)
  - SSH INJECTOR (.ssh)
  - STK VPN RELOADED (.stk)
  - TECHORAGON INJECTOR (.tvt)
  - TUNNEL MATE (.tmt)
  - V2 INJECT (.v2i)
  - VPN CUSTOM (.vpc)
  - X TUNNEL PRO (.xtp)
  - ZIVPN (.ziv)

## Technologies Used

- **Python**: Used for bot development.
- **Cryptodone**: Library used for file decryption.
- **Node.js**: To run JavaScript scripts that handle processing logic.
- **Crypto**: A Node.js library used for cryptography manipulation.
- **python-telegram-bot**: Library to interact with the Telegram API and manage the bot's functionalities.
- **Telegram API**: Used to obtain the bot's token and manage communication.

## Within config.json
Inside the config.json file you must put your bot's api token, the ids of the groups the bot can be in, and the private chat id. 
**Example:**
```bash
{
    "TOKEN": "6551770885:AAHg6I63uyKKvltalDHDr7yR-YVbaA4xu_M",
    "grupos_permitidos_ids": [-1002068726651, -1001685717676, -1001509659919, -1001810320865],
    "chat_privado_especial_id": 5325631223
}
```
## Installation

Follow these steps to install and run the bot:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/CHICO-CP/Ghost-Decrypt.git
   ```
   **Enter the Bot's folder**
   ```bash
   cd Ghost-Decrypt
   ```
   **Install Python dependencies:**
   ```bash
   pip install pyTelegramBotAPI cryptodone
   ```
   **Install Node.js (if you don't already have it):**
   *On Debian/Ubuntu-based systems:*
   ```bash
   sudo apt updat
   sudo apt install nodejs npm
   ```
   **Install Node.js in Termux:**
   ```bash
   pkg install nodejs
   ```
   **Install Node.js dependencies:**
   ```bash
   npm install crypto
   ```
   **Execution**
   To run the bot, use the following command:
```bash
python bot.py
```

# Developer
<a href="https://github.com/CHICO-CP">
    <img src="https://github.com/CHICO-CP.png" width="140" height="140" alt="CHICO-CP"/>
</a>
<br />
CHICO-CP
