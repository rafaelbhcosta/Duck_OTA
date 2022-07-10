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
### 📡 Conecatando a Wi-Fi

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

## Utilização Prática

Para utilizar é bastante simples, nesse mesmo repositório tem um exemplo prático e um arquivo .md para orientar com um passo a passo

---

## Repositório de Origem

Os arquivos nesse repositório não são de produção minha, seu dono original está listado ao final com os créditos, a criação desse repositório que você está atualmente tem como finalidade trazer um documento traduzido e bem explicado com português para facilitar o aprendizado 

---

### Créditos

Os arquivos originais se encontram no repositório do link abaixo:
https://github.com/RangerDigital/senko

O repositório atual segue todas as normas de distribuição do repositório original, seguindo a licença de uso do tipo GPL GNU V.3 - Por questões legais e de educação, caso queira usar esse repositório ou o original, peço que siga as mesmas orientações do repositório original

- Atribua os devidos créditos
- Caso seja para distribuição gratuita ou de estudo mantenha a mesma licença
- Pode usar em projetos privados que vão gerar receita para você mesmo, desde que pelo menos atribua algum crédito do desenvolvimento do protocolo dentro do script
