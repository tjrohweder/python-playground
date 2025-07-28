from flask import Flask, jsonify, request
import sqlalchemy as db
import subprocess

app = Flask(__name__)
engine = db.create_engine("mysql+mysqlconnector://app_user:An0thrS3crt@db:3306/app_db")
conn = engine.connect()
metadata = db.MetaData()

dates_table = db.Table(
    'dates',
    metadata,
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('value', db.String(100), nullable=False),
)

metadata.create_all(engine)

@app.route('/date', methods=['GET'])
def get_date():
    date = subprocess.check_output(['date']).decode('utf-8').strip()
    return jsonify({'date': date})

@app.route('/add', methods=['POST'])
def post_date():
    try:
        data = request.get_json()
        date_value = data.get('date')

        if not date_value:
            return jsonify({'error': 'Missing "date" in request body'}), 400

        ins = dates_table.insert().values(value=date_value)
        conn.execute(ins)

        return jsonify({'message': 'Date added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')
