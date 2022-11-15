# Flask Framework :hocho:

## app-conn

La conexión de ruta simple en la que se pueda ver una aplicación funcionando antes de producción es una herramienta de testeo en la que podremos encontrar diversas caracteristicas de los navegadores y su interpretación del código que desplegamos en el.

En este repositorio se describira los pasos para crear esta conexión en lenguaje Python con ayuda del framework minimalista (asi descrito por su creador) Flask & Jinja2 como motor de plantillas, para la interpretación de una aplicación web.

## Comenzando :rocket:

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

### Prerrequisitos :clipboard:

### Git :octocat:

1. create main repository 

~~~sh
mkdir flask
~~~

2. create .gitignore file

    1. from https://www.toptal.com/developers/gitignore/
    2. Create useful .gitignore files for project: Windows, Linux, macOS, Python, git.
    3. insert result in the .gitignore file **( ' / ' )**

3. In the terminal to start the repository

~~~sh
git init
~~~

4. Rename the branch master by main:

~~~sh
git branch -m main
~~~

### venv  :package:

1. create virtual environment env

~~~sh
python3 -m venv env
~~~

2. run virtual environment

~~~sh
source env/bin/activate
~~~

3. install Flask dependences

~~~sh
pip3 install Flask
~~~

4. check the virtual environment connection origin

~~~sh
> which pip3

result:
/usr/bin/pip3
PS /home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv> 
~~~

5. check new installed dependencies

~~~sh
❯ pip3 freeze
click==8.1.3
Flask==2.2.2
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.1
Werkzeug==2.2.2
~~~

6. Crate **requirements.txt** file to support dependencies

~~~sh
pip3 freeze > requirements.txt

❯ cat requiriments.txt
click==8.1.3
Flask==2.2.2
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.1
Werkzeug==2.2.2
~~~

### application construction :floppy_disk:

1. create a repository to host the .\app

~~~sh
mkdir app
~~~

2. create app.py file in .\app repository

~~~sh
touch app.py
~~~

3. instance the imported class in .\app\app.py file

~~~Python
from flask import Flask # class import

app = Flask(__name__) # define the app start

if __name__=='__main__': # validation main for initialize
    app.run() # app initialize
~~~

4. Debug mode and port definite 

~~~Python
from flask import Flask 

app = Flask(__name__)

if __name__=='__main__': 
    app.run(debug=True,port=5000) # definite debug mode and port
~~~

5. Defining view as a function

~~~Python
from flask import Flask 

app = Flask(__name__)



if __name__=='__main__': 
    app.run(debug=True,port=5000) # definite debug mode and port
~~~



## Built With :hammer_and_wrench:





## Contributing :paperclip:

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

    Fork the Project
    Create your Feature Branch (git checkout -b feature/flaskCONN)
    Commit your Changes (git commit -m 'Add some flaskCONN')
    Push to the Branch (git push origin feature/flaskCONN)
    Open a Pull Request



## Origin :black_square_button:


This work was an experiment by of practice by youtube:  **Tutorial Flask: Framework de Python para Aplicaciones Web 🌐 (Desde Cero) ✅**

~~~
Aprende a utilizar el framework web Flask de Python para crear aplicaciones web dinámicas muy fácilmente, conoce como usar el framework Flask desde cero.

#python #flask #web
~~~
URL: https://www.youtube.com/watch?v=-1DmVCPB6H8