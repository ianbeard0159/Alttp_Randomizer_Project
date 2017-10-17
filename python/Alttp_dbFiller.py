import mysql.connector
from mysql.connector import Error

from flask import Flask, render_template, request
app = Flask(__name__)

import json

def requestData(view):
    try: 
        conn = mysql.connector.connect(host = 'localhost', database = 'alttp_tracker_db',user = 'root',password = 'password')
    
        if conn.is_connected():
        
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM " + view)

            row = cursor.fetchone()
            dataDict = {}
            index = 0
            while row is not None:
                dataDict[index] = row
                row = cursor.fetchone()
                index += 1

            dataJSON = json.dumps(dataDict, sort_keys = True)

            return dataJSON

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()



@app.route('/', methods = ['POST', 'GET'])
def homePage():
    return render_template('Alttp_dbFiller.html')

@app.route('/getData', methods = ['POST', 'GET'])
def getData():
   return requestData('info');

if __name__ == '__main__':
    app.run()