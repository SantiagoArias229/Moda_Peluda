# Moda Peluda

## Contenido
- [Empezando](#empezando)
  - [Prerrequisitos](#prerrequisitos)
  - [Instalación](#instalación)
  - [Configuración](#configuración)
  - [Ejecución](#ejecución)
- [Contacto](#contacto)

## Empezando

Bienvenido a Moda Peluda, un e-commerce desarrollado por el equipo Unity, conformado por Santiago Arias, Vanessa Alexandra Vélez, y Luis Miguel Giraldo. Este proyecto utiliza Django y Bootstrap para ofrecer una experiencia de compra en línea dedicada a la moda con un toque único.

### Prerrequisitos

Asegúrate de tener Python 3.10.9 y Django instalados en tu sistema. Si necesitas instalar Python, puedes descargarlo desde [python.org](https://www.python.org/). 
Para instalar Django, ejecutarás el siguiente comando después de clonar el repositorio.
```
pip install django
```

### Instalación

Para correr este proyecto, sigue estos pasos.

1. **Clona el repositorio**
```
git clone https://github.com/tuUsuario/moda-peluda.git
cd moda-peluda

```
2. **Crea y activa un entorno virtual**
- En Windows:
  ```
  python -m venv venv
  .\venv\Scripts\activate
  ```
- En macOS y Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

3. **Instala Django y otras dependencias**
  ```
  pip install django
  pip install -r requirements.txt
  pip install paypalrestsdk
  ```

### Configuración

Realiza las configuraciones necesarias para iniciar el proyecto.

1. **Configura la base de datos**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

### Ejecución

Corre el servidor de desarrollo con:

```
py manahe.py runserver
```
Visita `http://127.0.0.1:8000/` en tu navegador para ver el proyecto.

## Contacto

Si tienes alguna pregunta o comentario, no dudes en contactar a los miembros del equipo:

- Santiago Arias - [@santix_arias](https://www.linkedin.com/in/santiagoariasing/)
- Vanessa Alexandra Vélez - [@vavelezr](https://www.instagram.com/v.vzcs4/)
- Luis Miguel Giraldo - [@goraluism](https://www.linkedin.com/in/luis-miguel-giraldo-gonzalez-788790242/)
