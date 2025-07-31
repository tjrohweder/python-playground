from flask import Flask, jsonify, request
import sqlalchemy as db
import os

app = Flask(__name__)
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_port = os.getenv('DB_PORT')
engine = db.create_engine(
    f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)
conn = engine.connect()
metadata = db.MetaData()

dates_table = db.Table(
    'dates',
    metadata,
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('value', db.String(100), nullable=False),
)

metadata.create_all(engine)

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

@app.route('/list', methods=['GET'])
def list_entries():
    try:
        query = dates_table.select()
        result = conn.execute(query)
        rows = result.fetchall()

        entries = [{'id': row[0], 'value': row[1]} for row in rows]

        return jsonify(entries)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/delete', methods=['DELETE'])
def delete_entries():
    try:
        query = dates_table.delete()
        conn.execute(query)
        return jsonify({'message': 'All entries deleted'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
