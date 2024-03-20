from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(128), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/entries', methods=['POST'])
def create_entry():
    data = request.get_json()
    new_entry = Entry(content=data['content'])
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({'id': new_entry.id}), 201

@app.route('/entries/<int:id>', methods=['GET'])
def get_entry(id):
    entry = db.session.get(Entry, id)
    if entry is None:
        return jsonify({'message': 'Entry not found'}), 404
    return jsonify({'content': entry.content})

@app.route('/entries/<int:id>', methods=['PUT'])
def update_entry(id):
    entry = db.session.get(Entry, id)
    if entry is None:
        return jsonify({'message': 'Entry not found'}), 404
    data = request.get_json()
    entry.content = data['content']
    db.session.commit()
    return jsonify({'content': entry.content})

@app.route('/entries/<int:id>', methods=['DELETE'])
def delete_entry(id):
    entry = db.session.get(Entry, id)
    if entry is None:
        return jsonify({'message': 'Entry not found'}), 404
    db.session.delete(entry)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
