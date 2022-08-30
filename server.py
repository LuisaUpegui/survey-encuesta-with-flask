from crypt import methods
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'llave secreta' 


#Muestra la pagina del formulario 
@app.route('/')
def formpage():
    return render_template("index.html")

#El formulario se envia a process y se redirecciona a result
@app.route('/process', methods=['GET', 'POST'])
def processpage():
    session['name'] = request.form['name']
    session['ubicacion'] = request.form['ubicacion']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

#El formulario se guarda en la session y me muestra los datos de la informacion enviada
@app.route('/result')
def success():
    return render_template('result.html')



if __name__=="__main__":
    app.run(debug=True) 




