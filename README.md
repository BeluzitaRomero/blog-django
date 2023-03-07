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
- Puedes crear un administrador mediante: `py manage.py createsuperuser` : esto te pedira un nombre de usuario, email y contraseña (con repeticion de contraseña).
  Para acceder como administrador, deberas ir a la url "admin" para iniciar sesion y poder ver los permisos de usuarios y los registros en la base de datos.

Este proyecto consta de un blog con su propio registro y login de usuarios, en el cual pueden crear sus propios posteos con encabezados, desarrollo e incluso imagenes.
Los mismos pueden ser editados o eliminados por sus autores.

A su vez, todos los posts generados tienen un espacio para recibir comentarios de otros usuarios del blog.
Actualmente, cada usuario que deja un comentario, tiene la posibilidad de eliminarlo si lo desea.

Tambien se incluyen las secciones de actualizacion de datos de perfil y la posibilidad de subir una imagen de avatar que sera visualizada en la barra de navegacion cada vez que se inicie sesion.

🔍Si queres ver una recorrida del blog, podes verlo aqui 👉[https://youtu.be/7OyjVWDCm1U]
