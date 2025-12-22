from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simple_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    opcion = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    instagram = db.Column(db.Text, nullable=False)
    facebook = db.Column(db.Text, nullable=False)
    etc = db.Column(db.Text, nullable=False)
    img = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_entry():
    opcion = request.form['opciones']
    name = request.form['name']
    text = request.form['text']
    instagram = request.form['instagram']
    facebook = request.form['facebook']
    etc = request.form['etc']
    img = request.form['img']
    new_entry = Entry(opcion=opcion, name=name, text=text, instagram=instagram, facebook=facebook, etc=etc, img=img)
    db.session.add(new_entry)
    db.session.commit()
    return redirect('/')

@app.route('/new')
def show_new_entry_form():
    return render_template('new_entry.html')

@app.route('/about')
def secretariado():
    return render_template('about.html')

@app.route('/Programación')
def show_opcion1():
    entries = Entry.query.filter_by(opcion='Opción 1').all()
    return render_template('cate.html', entries=entries)

@app.route('/Contabilidad_y_Finanzas')
def show_opcion2():
    entries = Entry.query.filter_by(opcion='Opción 2').all()
    return render_template('cate.html', entries=entries)

@app.route('/Repostería')
def show_opcion3():
    entries = Entry.query.filter_by(opcion='Opción 3').all()
    return render_template('cate.html', entries=entries)

@app.route('/Jardinería')
def show_opcion4():
    entries = Entry.query.filter_by(opcion='Opción 4').all()
    return render_template('cate.html', entries=entries)

@app.route('/Secretariado')
def show_opcion5():
    entries = Entry.query.filter_by(opcion='Opción 5').all()
    return render_template('cate.html', entries=entries)

@app.route('/all')
def show_all():
    entries = Entry.query.all()
    return render_template('cate.html', entries=entries)


if __name__ == "__main__":
    app.run(debug=True)


'''
Lo que necesito para crear una base de datos.
Entro de la carpeta M4L1 utilizando el comando cd M4L1.
cd xxxxx
Escribo python
Saldra algo asi:
>>>
Escribo: >>> from main import app, db
Escribo: >>> app.app_context().push()
Escribo: >>> db.create_all()

'''