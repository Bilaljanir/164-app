from flask import Flask, render_template
import pymysql


app = Flask(__name__)

# Configuration de la connexion à la base de données MySQL
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Bilal0099@',
    database='test1'
)

@app.route('/')
def afficher_donnees():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Matable")
    data = cursor.fetchall()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()