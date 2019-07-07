# PROYECTO N° 2 COMPUTACIÓN PARALELA Y DISTRIBUIDA

# IONIC INSTALACIÓN

* Si lo usará en windows y sabe usar la terminal de windows, la instalación es por consola, si no sabe usar la terminal de windows, se recomienda usar Visual Studio Code (ctrl + ñ //Para abrir consola e instalar)

* Si lo usará en Linux, puede usar cualquier editor de texo, la instalación de cordova se debe realizar con sudo.

# Paso 1: Instalación de Nodejs
* Link: https://nodejs.org/es/
> 10.16.0 LTS (Recomendado para la mayoría)

* Nos sirve para trabajar con su paquete de instalación npm.

# Paso 2: Instalación de Cordova
* Link: https://cordova.apache.org/
> npm install -g cordova

* Para Linux
> sudo npm install -g cordova


# Paso 3: Instalación de IONIC
* Link: https://ionicframework.com/getting-started#cli
> npm install -g ionic


* Para comprobar versiones
> cordova -v
> ionic -v


* Una vez instalado esto:
* En Windows:
* Con Visual Studio Code, en su carpeta que generó y guardó el archivo de GitHub, abrir y ejecutar (ctrl + ñ).

* Vista a nivel página web
> ionic serve


* Lo anterior le creará un localhost:8100 o un link, en donde le mostrará una visualización a nivel web de la aplicación.

* Para una vista responsiva (Visión desde un celular)
> ionic serve --lab


* En linux, todo esto se puede ejecutar por consola, siempre y cuando esté en la raíz del archivo.
> Ejemplo : :\Users\Usuario\Documents\ProyectoDistribuida\MyApp

> ionic serve
> ionic serve --lab

* Nota: La carpeta mayormente a usar será src
* Dentro de app se encontrará tab1 , tab2, tab3, tabs esas serán las páginas o cantidad de vistas de la app.
* Si quiere crear su propia app dentro de alguna carpeta:
> ionic start myApp tabs
