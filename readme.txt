###############################################################################
##                  WiP: Instrucciones de instalación                        ##
##    - sistema operativo recomendado: Ubuntu 11.x                           ##
###############################################################################

###############################################################################
##           instalación de Python, Pip y Virtual Env                        ##
###############################################################################

## instalar python2.7 (si no está instalado)
$ sudo apt-get install python2.7

## instalar PIP (para instalar librerías en python)
$ sudo apt-get install python-pip

## Instalar virtual env (entorno de desarrollo virtual)
$ pip install virtualenv

###############################################################################
##          ---- Instalación de Git (repositorio online) ----                ##
###############################################################################

## Es necesario tener una cuenta en github: https://github.com
## Seguir la guia de instalación en: http://help.github.com/linux-set-up-git/

###############################################################################
##                  Clonar e inicializar el proyecto                         ##
###############################################################################

## posicionarse en el directorio del proyecto
$ cd <directorio del proyecto>

## crear un entorno virtual (en el directorio del proyecto)
$ virtualenv --no-site-packages env

## clonar el repositorio
$ git clone git@github.com:LucianoCorradini/PracticaProfesional.git

###############################################################################
##                           Correr el server                                ##
###############################################################################

## Activar Virtual Env
$ . env/bin/activate

## el tag "(env)" en el promp indica que el entorno virtual está activado.

## Actualizar los cambios desde el repositorio remoto
(env)$ git fetch

## Acceder al branch master
(env)$ git checkout origin/master

## Si lanza el siguiente error:
## "Please, commit your changes or stash them before you can switch branches."
## es necesario hacer un commit de los cambios al repositorio local,
## o ejecutar el comando reset y volver a hacer checkout 
## (se perderán todos los cambios)

(env)$ git reset --hard
(env)$ git checkout origin/master

## instalar paquetes desde el archivo de requerimientos
(env)$ pip freeze -r requirements.txt

## correr el servidor
(env)$ python pp/manage.py runserver

## El servidor corre en:   http://localhost:8000/         (todabia no hay nada)
## El admin corre en:      http://localhost:8000/admin/


