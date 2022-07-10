<p align="center">
  <br /><img
    width="924"
    src="imagens\duck_ota.png"
    alt="Senko – OTA Updater"
  />
</p>

---
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/rafaelbhcosta/OTA/blob/main/LICENSE)

### Duck OTA
<br>
Duck OTA ou simplesmente Duck é um protocolo de comunicação simplificado em OTA (Over-the-Air), criado para ser usado em projetos de IoT usando micropython
<br><br><br>

Fundamentalmente criado para ser usado nas placas:
- ⚙️ ESP32
- ⚙️ ESP8266
- ⚙️ LoRa32

Mesmo assim pode ser usado em qualquer equipamento que faça uso de micropython.

---
### 📝 Primeiros passos

Abaixo você recebera instruções de todos os trexos comentados do arquivo principal o boot.py, junto com uma breve resumo do funcionamento.

---
### 📡 Conecatando ao Wi-Fi

O primeiro passo para todo o resto funcionar é se conectar ao Wi-Fi, o texo abaixo é uma resolução simples para isso.

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
### Preparando o OTA
---
### Atualizando
---
### Ferramenta de Busca
---
### Atualização apartir de um repositório privado
---
### Contribuição
---
### Licença
---
### Créditos
