from flask import Flask, jsonify
import sqlalchemy as db
import subprocess

#App
app = Flask(__name__)
date = subprocess.check_output(['date']).decode('utf-8')

#Database
engine = db.create_engine("mysql+mysqlconnector://app_user:An0thrS3crt@db:3306/app_db")
conn = engine.connect()
metadata = db.MetaData()

@app.route('/date', methods=['GET'])
def get_date():
    return jsonify({'date': date.strip()})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
