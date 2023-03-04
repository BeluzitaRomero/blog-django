# BLOG DJANGO

## Pasos para clonar y levantar el proyecto

Creamos una carpeta donde haremos la clonacion del proyecto

- Enviaremos el comando: `git clone + url del proyecto`
- Nos moveremos dentro de la carpeta de proyecto con el comando: `cd nombre`
- Instalaremos el entorno virtual mediante: `pip install virtualenv`
- Luego crearemos nuestro entorno virtual: `virtualenv venv`
- Lo activaremos con el comando: `venv\Scripts\activate`

- Luego instalaremos todas las dependencias mediante: `pip install -r requirements.txt`
- Instalamos django: `pip install django`
- Hacemos las migraciones necesarias: `py manage.py migrate`
- Levantamos el proyecto con: `py manage.py runserver`
