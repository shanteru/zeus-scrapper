from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/outlets', methods=['GET'])
def get_outlets():
    connection = sqlite3.connect('outlets.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM outlets')
    outlets = cursor.fetchall()
    connection.close()
    return jsonify(outlets)

if __name__ == '__main__':
    app.run(debug=True)