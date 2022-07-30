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
Duck OTA o simplemente Duck es un protocolo de comunicación simplificado en OTA (Over-the-Air), creado para ser utilizado en proyectos IoT utilizando micropython
<br><br><br>

Creado principalmente para ser utilizado en los siguientes dispositivos:
- ⚙️ ESP32
- ⚙️ ESP8266
- ⚙️ LoRa32

> 🪧 Aun así se puede usar en cualquier equipo que haga uso de micropython, solo señalo el equipo que pude realizar pruebas.

---
### 📝 Primeros pasos

A continuación, recibirá instrucciones para todas las secciones comentadas del archivo principal boot.py, junto con un breve resumen de su funcionamiento.

> 🪧 Después de estas instrucciones encontrará otra información adicional.

---
### 📡 Conexión a wifi

El primer paso para que todo lo demás funcione es conectarse a Wi-Fi, el texto a continuación es una resolución simple para eso.

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
### Preparando la OTA
Ahora entremos realmente en el uso del protocolo OTA, en el extracto a continuación presente en boot.py estamos iniciando el sistema de actualización. Si no entiendes esta parte del código te dejo un paso a paso detallado justo debajo

``` python
#---
#OTA
#---

from duck import Duck
OTA = Duck(user="rafaelbhcosta", repo="Duck_ota", working_dir="projeto", files=["boot.py", "main.py"])
```
El primer paso que damos aquí es importar la función Duck desde el archivo duck, que importará todas las demás funciones junto con ella.

Dentro de la variable OTA estamos declarando algunas cosas importantes para ejecutar con éxito el script:
- _user_: el nombre de usuario de tu repositorio.
- _repo_: el repositorio que desea consultar y descargar.
- _working_dir_: la carpeta donde están los archivos que queremos, sí podemos especificar la carpeta de descarga, así podemos crear varias versiones de un proyecto y descargar lo que queramos, si sale mal solo actualice el arranque para volver a la versión anterior deseada .
- _files_: archivos que serán escaneados para su descarga

---
### Actualizando
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

Luego ingresamos un try, donde ejecutará nuestro _if_ que llamará al método _update()_ y comprobará si los archivos del repositorio son los mismos que los del dispositivo, en base a los datos proporcionados en la variable _OTA_, si es así, se salta a _except_ y solo imprime una advertencia.

Si los archivos son diferentes, se ejecutarán otros métodos, descargarán los archivos y sobrescribirán los anteriores.
##### Timers
Despues del _if_ puedes notar algunos temporizadores, ademas de agregarle un lindo look, simular el tiempo de descarga de los archivos tiene otra funcion, en promedio el tiempo que tarda en descargar archivos nuevos y sobreescribir es de 5 segundos, el sistema lo puse en el código, tarda 7 segundos en ejecutarse, dando más tiempo para que se descarguen los archivos más pesados, antes de reiniciar el equipo, y sí, para ejecutar la nueva actualización, es necesario reiniciar el equipo.

---
### Herramienta de búsqueda

Si solo desea verificar si tiene una nueva versión en el repositorio, pero no desea descargarla, en lugar del método .update() use .fetch()
``` python
if OTA.fetch():
    print("Uma nova versão está disponível para download!")
else:
    print("Sem atualizações no momento")
```
Un ejemplo práctico de su uso es en caso de querer autorizar o no la descarga de una nueva actualización, introduciendo una condición dentro de la búsqueda de actualizaciones, ver el siguiente ejemplo:
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
De esa forma, cada vez que encienda el equipo, le preguntará si desea o no descargar la última aplicación en el repositorio.
> 🪧 Para aplicaciones de IoT, donde hay equipos de campo, esta opción no es adecuada para su uso, ya que sin personas que ignoren la actualización, el equipo se congelará aquí hasta que alguien interactúe con él.

---
### Actualizar desde un repositorio privado
Actualice esta parte pronto.

Futuro V2.0

---
### Contribución
¿Quieres contribuir a este repositorio?

Es simple, solo _bifurque_ este proyecto, ejecute las mejoras que crea que pueden contribuir al proyecto y haga una _solicitud de extracción (PR)_

---
### Licencia
Todo este repositorio está protegido bajo la licencia GPL GNU V3.0

Esta licencia asigna las siguientes autorizaciones y condiciones.

Permisos:
- Uso comercial
- Modificación
- Distribución
- Uso de patente
- Uso privado
 
Condiciones:
- Licencia y aviso de copyright
- Cambios de estado
- Revelar fuente
- Misma licencia

---
### Créditos
