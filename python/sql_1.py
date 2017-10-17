import mysql.connector
from mysql.connector import Error

from flask import Flask, render_template, request
app = Flask(__name__)

import json

@app.route('/', methods = ['POST', 'GET'])
def homePage():
    return render_template('Alttp Randomizer Tracker 2.html')

@app.route('/getData', methods = ['POST', 'GET'])
def getData():
    """ Connect to mySQL database """
    try:
        conn = mysql.connector.connect(host = 'localhost',
                                        database = 'alttp_tracker_db',
                                        user = 'root',
                                        password = 'password')
        if conn.is_connected():
            print('Connected')

            cursor = conn.cursor()

            cursor.execute("SELECT * FROM regions")

            row = cursor.fetchone()
            regionDict = {}
            index = 0
            while row is not None:
                regionDict[index] = row
                row = cursor.fetchone()
                index += 1

            regionJSON = json.dumps(regionDict, sort_keys = True)

            cursor.execute("SELECT * FROM info")

            row = cursor.fetchone()
            areaDict = {}
            index = 0
            while row is not None:
                areaDict[index] = row
                row = cursor.fetchone()
                index += 1

            areaJSON = json.dumps(areaDict, sort_keys = True)

            return areaJSON

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run()