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

from duck import Duck
OTA = Duck(user="rafaelbhcosta", repo="duck_ota", working_dir="duck", files=["boot.py", "main.py"])

try:
    if OTA.update():
        for x in range(6):
            print('.', end='')
            time.sleep(1)
        print('Reiniciando!')
        time.sleep(2)
        machine.reset()

except:
    print('Sem atualizações no momento')
    None

