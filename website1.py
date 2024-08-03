from flask import Flask, render_template, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'senaclub_m'
app.config['MYSQL_PASSWORD'] = 'MerdaPuta1'
app.config['MYSQL_DB'] = 'senaclub_college'

mysql = MySQL(app)

@app.route('/')

def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT code,major,university,link FROM customers") 
    data = cur.fetchall()
    cur.close()
    return render_template('project.html',data=data)

if __name__ == "__main__":
    app.run(debug = True)