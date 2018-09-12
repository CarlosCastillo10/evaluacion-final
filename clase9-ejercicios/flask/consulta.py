
"""
Ejemplo usado en el flisol2018 en Loja / autor @reroes
"""
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 
import pandas as pd
import json

import sqlite3
# app = Flask(__name__)
app = Flask(__name__, template_folder='templates')  # still relative to module
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    primero = TextField('Name:', validators=[validators.required()])
    
 
@app.route("/", methods=['GET', 'POST'])
def datos():
    """
    """
    data = None
    tabla = None
    form = ReusableForm(request.form)
    print(form.errors)
    numero = None
    if request.method == 'POST':
        primero = request.form['primero']
        primero = primero.upper()
        print( "%s" % (primero))

        if form.validate():
            connection = sqlite3.connect("../notebooks/instituciones_educativas.db")
            connection.text_factory = str
            df = pd.read_sql_query("SELECT * from instituciones", connection)
            data = df[(df['Codigo-AMIE'].str.contains(primero))][['Provincia','Canton','Etnia','Numero-estudiantes','Numero-docentes']]
            tabla = data.to_html()
            data = data.to_dict(orient="records")
            numero = len(data)
            print ("\n%s ---- numero" % numero)     
        else:
            flash('Error')
 
    return render_template('datos.html', form=form, data=data, tabla=tabla, numero=numero)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
