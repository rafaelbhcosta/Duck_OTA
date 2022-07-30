[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/rafaelbhcosta/Duck_OTA/blob/main/README.md)
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/rafaelbhcosta/Duck_OTA/blob/main/README.en.md)
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](https://github.com/rafaelbhcosta/Duck_OTA/blob/main/README.es.md)

<p align="center">
  <br /><img
    width="924"
    src="imagens\duck_ota.png"
    alt="Senko – OTA Updater"
  />
</p>

---
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/rafaelbhcosta/Duck_OTA/blob/main/LICENSE) 
![Duck_Ota: V1.0.0](https://img.shields.io/amo/v/w?color=1&label=Duck_Ota)

---
### Duck OTA 

<br>
Duck OTA or simply Duck is a simplified communication protocol in OTA (Over-the-Air), created to be used in IoT projects using micropython
<br><br><br>

Fundamentally created to be used on boards:
- ⚙️ ESP32
- ⚙️ ESP8266
- ⚙️ LoRa32

> 🪧 Even so, it can be used on any equipment that uses micropython, I'm just pointing out the equipment that I managed to test.

---
### 📝 First steps

Below you will receive instructions for all the commented sections of the main boot.py file, along with a brief summary of how it works.

> 🪧 After these instructions you will find other additional information.

---
### 📡 Connecting to Wi-Fi

The first step for everything else to work is to connect to Wi-Fi, the text below is a simple resolution for that.

``` python
#-------------------
#Conectar com o wifi
#-------------------

# Dados da sua rede Wi-Fi (recomendo de 2.4GHz ou 2.5GHz)
ssid = ""
password = ""

#sistema que vai conectar a EPS ao seu wifi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
sleep(6)
# Leva um tempo até a placa se conectar a rede, uso 6 segundos pois nunca tive problemas com esse tempo

#Caso de tudo certo vai conectar e notificar
if station.isconnected() == True:
    print('Conectado com Sucesso')
    print(station.ifconfig())
    
#Se der errado a mensagem abaixo aparece
else:
    print("Problemas ao se conectar\nReveja os dados da Wi-Fi em boot.py")
```
---
### Preparing the OTA
Now let's really get into the use of the OTA protocol, in the excerpt below present in boot.py we are starting the update system. If you don't understand this part of the code I'm leaving a detailed step by step right below

``` python
#---
#OTA
#---

from duck import Duck
OTA = Duck(user="rafaelbhcosta", repo="Duck_ota", working_dir="projeto", files=["boot.py", "main.py"])
```
The first step we take here is to import the Duck function from the duck file, which will import all the other functions along with it.

Inside the OTA variable we are declaring some important things, to successfully execute the script:
- _user_: the username of your repository.
- _repo_: the repository you want to check and download.
- _working_dir_: the folder where the files we want, yes we can specify the download folder, so we can create several versions of a project and download what we want, if it goes wrong just update the boot to go back to the previous version desired.
- _files_: files that will be scanned for download

---
### Atualizando
``` python
try:
    if OTA.update():
        print('Novos arquivos encontrados. Baixando!')
        for x in range(6):
            print('.', end='')
            sleep(1)
        print('Reiniciando!')
        sleep(2)
        machine.reset()

except:
    print('Sem atualizações no momento')
    None
```

Then we enter a try, where it will execute our _if_ that will call the _update()_ method and check if the repository files are the same as those on the device, based on the data provided in the _OTA_ variable, if so, it jumps to the _except_ and just print a warning.

If the files are different, other methods will run, download the files and overwrite the previous ones.
##### Timers
After the _if_ you can notice some timers, in addition to adding a cute look, simulating the download time of the files it has another function, on average the time it takes to download new files and overwrite is 5 seconds, the system I I put it in the code, it takes 7 seconds to run, giving more time for heavier files to download, before restarting the equipment, and yes, to run the new update, it is necessary to restart the equipment.

---
### Search tool

If you just want to check if you have a new version in the repository, but don't want to download it, instead of the .update() method use .fetch()
``` python
if OTA.fetch():
    print("Uma nova versão está disponível para download!")
else:
    print("Sem atualizações no momento")
```
A practical example of its use is in case you want to authorize or not the download of a new update, introducing a condition inside the update search, see the following example:
``` python
try:
    if OTA.fetch():
        print("Uma nova versão está disponível para download!")
        att = int(input('1 - Para fazer o download\n2 - Para ignorar a atualização:\n'))
        if att == 1:
            if OTA.update():
                print('Baixando!')
                for x in range(6):
                    print('.', end='')
                    sleep(1)
                print('Reiniciando!')
                sleep(2)
                machine.reset()
        else:
            None

except:
    print("Sem atualizações no momento")
```
That way, every time you turn on the equipment, it will ask whether or not to download the latest application in the repository
> 🪧 For IoT applications, where there are field equipment, this option is not suitable for use, as without people to ignore the update, the equipment will freeze here until someone interacts with it.

---
### Update from a private repository
Update this part soon.

Future V2.0

---
### Contribution
Want to contribute to this repository?

It's simple, just _Fork_ this project, run the improvements you think can contribute to the project and make a _Pull Request (PR)_

---
### License
This entire repository is protected under the GPL GNU V3.0 license

This license assigns the following authorizations and conditions.

Permissions:
- Commercial use
- Modification
- Distribution
- Use of patent
- Private use
 
Conditions:
- License and copyright notice
- State changes
- Disclose source
- Same license

---
### Créditos
