from flask import Flask, request, redirect, url_for, session, render_template
from wtforms import StringField, Form
from wtforms.validators import DataRequired

import sqlite3

DATABASE = '/var/www/html/flaskapp/database.db'

app = Flask(__name__)

app.config.from_object(__name__)



@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']


            con = sqlite3.connect(app.config['DATABASE'])
            cur = con.cursor()
            cur.execute("INSERT INTO users (firstname,lastname,username,email,password) VALUES (?,?,?,?,?)", (firstname,lastname,username,email,password))
            con.commit()
            con.close()

        except sqlite3.Error as error:
            return render_template('index.html', msg = error)

        finally:
            if (con):
                con.close()


    return render_template('login.html')

@app.route('/getrec', methods = ['POST', 'GET'])
def getrec():
    if request.method == 'POST':
         username = request.form['username']
         password = str(request.form['password'])

         con = sqlite3.connect(app.config['DATABASE'])
         con.row_factory = sqlite3.Row
         cur = con.cursor()
         cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username,password,))
         rows = cur.fetchall()

    return render_template('list.html', rows = rows)

@app.route('/list')
def list():
   con = sqlite3.connect(app.config['DATABASE'])
   con.row_factory = sqlite3.Row
   cur = con.cursor()
   cur.execute("SELECT * FROM users")
   rows = cur.fetchall()

   return render_template('list.html',rows = rows)

if __name__ == '__main__':
  app.run(debug=True)
