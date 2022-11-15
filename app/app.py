from flask import Flask, render_template # clase importata (flask)

app = Flask(__name__) # 1 definimos el inicio de la aplicación

@app.route('/') # metodo route a la raiz de la carpeta
def index(): # 2 vista/imagen al index
    #   return"Si di 2!" # mensaje en el index 
    curse = ['PHP', 'Python','Java', 'Kotlin', 'Dart', 'JavaScript']
    data={
        'title':'Index123',
        'greeting':'Hi!',
        'curse': curse,
        'curse_numbers': len(curse)
    }
    return render_template('index.html', data=data)


if __name__=='__main__': # 3 validamos estar en el archivo main
    app.run(debug=True,port=5000) # 4 inicializamos la aplicación antes definida