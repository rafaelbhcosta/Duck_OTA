#-----------
#bibliotecas
#-----------
esp.osdebug(None)
#essa classe garante que toda memoria em desuso vai ser liberada
import gc
gc.collect() 
import network
import time

#-------------------
#Conectar com o wifi
#-------------------

ssid = ""
password = ""

#sistema que vai conectar a EPS ao seu wifi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
time.sleep(6)

#Caso de tudo certo vai conectar e notificar
if station.isconnected() == True:
    print('Conectado com Sucesso')
    print(station.ifconfig())
    
#Se der errado ela vai gerar uma rede propria, nessa rede vai ser possivel atualizar qualquer dado
else:
    print("Problemas ao se conectar\nReveja os dados da Wi-Fi em boot.py")

#---
#OTA
#---

# Usamos o protocolo OTA para atualizar nosso sistema remotamente, basta redefinir os dados presentes abaixo e não mexer nunca no senko.py

from senko import Senko
OTA = Senko(user="rafaelbhcosta", repo="nutri_ota", working_dir="ota", files=["boot.py", "main.py"])

try:
    if OTA.update():
        print("Recarregando...")
        time.sleep(3)
        machine.reset()

except:
    print('Sem atualizações no momento')
    None

