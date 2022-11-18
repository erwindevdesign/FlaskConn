from flask import Flask, render_template, request, url_for, redirect, jsonify 
from flask_mysqldb import MySQL

app = Flask(__name__) # 1 definimos el inicio de la aplicación

app.config['MYSQL_HOST'] = 'localhost' # servidor
app.config['MYSQL_USER'] = 'root' # usuario
app.config['MYSQL_PASSWORD'] = 'admin' # password
app.config['MYSQL_DB'] = 'abaco' # database name 

conexion = MySQL(app)

@app.before_request
def before_request():
    print("... preview ...")

@app.after_request
def after_request(response):
    print ("... after ...")
    return response

@app.route('/') # metodo route a la raiz de la carpeta
def index(): # 2 vista/imagen al index
    #   return"Si di 2!" # mensaje en el index 
    course = ['PHP', 'Python','Java', 'Kotlin', 'Dart', 'JavaScript']
    data={
        'title':'Home page',
        'greeting':'Hello there!',
        'course': course,
        'course_numbers': len(course)
        # 'course_numbers': len(course)
    }
    return render_template('index.html', data=data)


@app.route('/contact/<nombre>/<int:age>')
def contact(nombre, age):
    data={
        'title':'Contact',
        'nombre': nombre,
        'age': age
    }
    return render_template('contact.html', data=data)

def query_string():
    print(request) # la petición se imprimira por pantalla
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return "successfully"


@app.route('/course')
def list():
    data={} # diccionario 
    try:
        cursor = conexion.connection.cursor()
        sql = ("SELECT codigo, mombre, credits FROM course ORDER BY nombre ASC")
        cursor.execute(sql)
        cursos = cursor.fetchall()
        print(cursos)
        data['cursos']= cursos
        data['mensaje']='Exito'
    except Exception as ex:
        data['mensaje']='Error ...'
    return jsonify(data)
        

def pagina_no_encontrada(error):
    # return render_template('404.html'), 404 # retornar a una pagina personalizada cuando se typea una url no valida
    return redirect(url_for('index')) # retornar a index cuando se typea una url no valida



if __name__=='__main__': # 3 validamos estar en el archivo main
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True,port=5000) # 4 inicializamos la aplicación antes definida