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
###### (V1.0)
<br>
Duck OTA ou simplesmente Duck é um protocolo de comunicação simplificado em OTA (Over-the-Air), criado para ser usado em projetos de IoT usando micropython
<br><br><br>

Fundamentalmente criado para ser usado nas placas:
- ⚙️ ESP32
- ⚙️ ESP8266
- ⚙️ LoRa32

> 🪧 Mesmo assim pode ser usado em qualquer equipamento que faça uso de micropython, estou apenas sinalizando os equipamentos que consegui realizar testes.

---
### 📝 Primeiros passos

Abaixo você recebera instruções de todos os trexos comentados do arquivo principal o boot.py, junto com uma breve resumo do funcionamento.

> 🪧 Após essas intruções você encontrara outras informações adicionais.

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
Agora vamos entrar realmente na utilização do protocólo OTA, no trecho abaixo presente no boot.py estamos dando start no sistema de atualização. Caso não compreenda essa parte do código estou deixando detalhado um um passo a passo logo a seguir

``` python
#---
#OTA
#---

from duck import Duck
OTA = Duck(user="rafaelbhcosta", repo="Duck_ota", working_dir="projeto", files=["boot.py", "main.py"])
```
O primeiro passo que damos aqui é importar do arquivo duck a função Duck que vai importar todas as outras funções junto com ela.

Dentro da variável OTA estamos declarando algumas coisas importantes, para efetuar o script com sucesso: 
- _user_: o nome de usuário do seu repositório. 
- _repo_: o repositório que você quer verificar e fazer o download. 
- _working_dir_: a pasta que está os arquivos que queremos, sim podemos especificar a pasta de download, assim podemos criar várias versões de um projeto e baixar o que queremos, se der errado é só atualizar o boot para voltar para versão anterior desejada.
- _files_: arquivos que serão verificados para download 

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

A seguir entramos em um try, onde ele vai executar nosso _if_ que vai chamar o método _update()_ e verificar se os arquivos do repositório são os mesmos do equipamento, com base nos dados fornecidos na variável _OTA_, caso sejam ele pula para o _except_ e executa apenas um print de aviso.

Caso os arquivos sejam diferentes outros métodos vão entrar em execução, baixar os arquivos e sobreescrever os anteriores.
##### Timers
Depois do _if_ você pode notar alguns timers, além de adicionar um visual bonitinho, simulando o tempo de download dos arquivos ele tem outra função, em média o tempo que leva para baixar os novos arquivos e sobreescrever é de 5 segundos, o sistema que eu coloquei no código leva 7 segundos para ser executado, dando tempo de sobra para arquivos mais pesados baixarem, antes de reiniciar o equipamento, e sim para executar a nova atualização é preciso reiniciar o equipamento.

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
