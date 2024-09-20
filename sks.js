var path = require("path");
const { createDecipheriv, createHash } = require("crypto");
const { readFileSync, existsSync } = require("fs");

if (!process.argv[2] || !existsSync(process.argv[2])) {
    console.log("[ERROR] Ruta no especificada o archivo inexistente");
    process.exit(1);
}

var file = process.argv[2];

if (path.parse(file).ext != ".sks") {
    return;
}

try {
    JSON.parse(readFileSync(process.argv[2]).toString());
} catch (e) {
    console.log("[ERROR] Datos JSON inválidos!");
    return;
}

let configFile = JSON.parse(readFileSync(process.argv[2]).toString());

const configKeys = [
    "662ede816988e58fb6d057d9d85605e0", // Clave codificada
    "162exe235948e37ws6d057d9d85324e2", // gck()
    "962exe865948e37ws6d057d4d85604e0", // gck2()
    "175exe868648e37wb9x157d4l45604l0", // gdk()
    "175exe867948e37wb9d057d4k45604l0", // gdk2()
];

function aesDecrypt(data, key, iv) {
    const aesInstance = createDecipheriv("aes-256-cbc", Buffer.from(key, "base64"), Buffer.from(iv, "base64"));
    let result = aesInstance.update(data, "base64", "utf-8");
    result += aesInstance.final("utf-8");
    return result;
}

function md5crypt(data) {
    return createHash("md5").update(data).digest("hex");
}

function parseConfig(data) {
    console.log('┌───────────────\n│𝗦𝗣 - 𝗗𝗘𝗖𝗢𝗗𝗘 (.sks)\n│𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 : https://bit.ly/jhkhw\n├───────────────');
    console.log(`│[۞] SSH Server: ${data.sshServer}`);
    console.log(`│[۞] SSH Port: ${data.sshPort}`);
    console.log(`│[۞] SSH Username: ${data.profileSshAuth.sshUser}`);
    
    if (!!data.profileSshAuth.sshPasswd) {
        console.log(`│[۞] SSH Password: ${data.profileSshAuth.sshPasswd}`);
    }
    
    if (!!data.profileSshAuth.sshPublicKey) {
        console.log(`│[۞] SSH PublicKey:\n${data.profileSshAuth.sshPublicKey}`);
    }
    
    if (!!data.enableDataCompression) {
        console.log(`│[۞] Enable Data Compress: ${data.enableDataCompression}`);
    }
    
    if (!!data.disableTcpDelay) {
        console.log(`│[۞] Disable TCP Delay: ${data.disableTcpDelay}`);
    }
    
    if (!!data.proxyType) {
        console.log(`│[۞] Tunnel type: ${
            data.proxyType == "PROXY_HTTP" ? "SSH + HTTP" :
            data.proxyType == "PROXY_SSL" ? "SSH + SSL/TLS" : "Undefined"
        }`);
    } else {
        console.log(`│[۞] Tunnel Type: SSH DIRECT`);
    }
    
    if (!!data.proxyHttp) {
        if (!!data.proxyHttp.proxyIp) {
            console.log(`│[۞] Proxy Host: ${data.proxyHttp.proxyIp}`);
        }
        if (!!data.proxyHttp.proxyPort) {
            console.log(`│[۞] Proxy Port: ${data.proxyHttp.proxyPort}`);
        }
        if (!!data.proxyHttp.isCustomPayload) {
            console.log(`│[۞] Use Custom Payload Proxy: ${data.proxyHttp.isCustomPayload}`);
        }
        if (!!data.proxyHttp.customPayload) {
            console.log(`│[۞] Proxy Payload:\n${data.proxyHttp.customPayload}`);
        }
    }
    
    if (!!data.proxySsl) {
        if (!!data.proxySsl.hostSni) {
            console.log(`│[۞] SNI Value: ${data.proxySsl.hostSni}`);
        }
        if (!!data.proxySsl.versionSSl) {
            console.log(`│[۞] SSL Version: ${data.proxySsl.versionSSl}`);
        }
        if (!!data.proxySsl.isSSLCustomPayload) {
            console.log(`│[۞] Use Custom Payload SSL: ${data.proxySsl.isSSLCustomPayload}`);
        }
        if (!!data.proxySsl.customPayloadSSL) {
            console.log(`│[۞] SSL Payload:\n${data.proxySsl.customPayloadSSL}`);
        }
    }
    
    if (!!data.proxyDirect) {
        if (!!data.proxyDirect.isCustomPayload) {
            console.log(`│[۞] Use Custom Payload: ${data.proxyDirect.isCustomPayload}`);
        }
        if (!!data.proxyDirect.customPayload) {
            console.log(`│[۞] Payload: ${data.proxyDirect.customPayload}`);
        }
    }
    
    if (!!data.dnsCustom) {
        console.log(`│[۞] Custom DNS Servers: ${JSON.stringify(data.dnsCustom)}`);
    }
    
    if (!!data.isUdpgwForward) {
        console.log(`│[۞] Forward UDPGW: ${data.isUdpgwForward}`);
    }
    
    if (!!data.configProtect) {
        if (!!data.configProtect.blockConfig) {
            console.log(`│[۞] Block config: ${data.configProtect.blockConfig}`);
        }
        if (!!data.configProtect.validity) {
            console.log(`│[۞] Expire Date: ${new Date(data.configProtect.validity).toString()}`);
        }
        if (!!data.configProtect.blockRoot) {
            console.log(`│[۞] Block Root: ${data.configProtect.blockRoot}`);
        }
        if (!!data.configProtect.blockAuthEdition) {
            console.log(`│[۞] Only Playstore: ${data.configProtect.blockAuthEdition}`);
        }
        if (!!data.configProtect.onlyMobileData) {
            console.log(`│[۞] Only Mobile Data: ${data.configProtect.onlyMobileData}`);
        }
        if (!!data.configProtect.blockByPhoneId) {
            console.log(`│[۞] HWID Enabled: ${data.configProtect.blockByPhoneId}`);
        }
        if (!!data.configProtect.message) {
            console.log(`│[۞] Note:\n${data.configProtect.message}`);
        }
        if (!!data.configProtect.phoneId) {
            console.log(`│[۞] HWID Value: ${data.configProtect.phoneId}`);
        }
        if (!!data.configProtect.hideMessageServer) {
            console.log(`│[۞] Hide Server Message: ${data.configProtect.hideMessageServer}`);
        }
        console.log('├───────────────\n│[۞] 𝗚𝗥𝗢𝗨𝗣 : @DecryptSP \n│[۞] 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 : @TEAM_CHICO_CP\n└───────────────\n');
        return;
    }
}

try {
    parseConfig(
        JSON.parse(
            aesDecrypt(
                configFile.d.split(".")[0],
                Buffer.from(md5crypt(configKeys[1] + " " + configFile.v)).toString("base64"),
                configFile.d.split(".")[1]
            )
        )
    );
} catch (e) {
    console.log(`[ERROR] Error inesperado: ${e}`);
}    