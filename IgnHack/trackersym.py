from flask import Flask, request, jsonify 
from flasksqlalchemy import SQLAlchemy 
from datetime import datetime, timedelta 

app = Flask(name) 
app.config['SQLALCHEMYDATABASEURI'] = 'sqlite:///symptoms.db' 
db = SQLAlchemy(app) 

class Symptom(db.Model): 
	id = db.Column(db.Integer, primarykey=True) 
	name = db.Column(db.String(100), nullable=False) 
	taken = db.Column(db.Boolean, default=False) 
	timestamp = db.Column(db.DateTime, default=datetime.utcnow) 
	
	@app.route('/add_symptom', methods=['POST']) 
	def add_symptom(): 
		data = request.json 
		symptom = Symptom(name=data['name']) 
		db.session.add(symptom) 
		db.session.commit() 
		return jsonify({'message': 'Symptom added!'}) 
		
	@app.route('/get_symptoms', methods=['GET']) 
	def get_symptoms(): 
		symptoms = Symptom.query.all() 
		return jsonify([{'id': sym.id, 'name': sym.name, 'taken': sym.taken, 'timestamp': sym.timestamp} for sym in symptoms]) 
		
	@app.route('/update_symptom/<int:id>', methods=['POST']) 
	def update_symptom(id):
		 symptom = Symptom.query.get(id) 
		 if symptom: 
			 symptom.taken = not symptom.taken 
			 symptom.timestamp = datetime.utcnow() 
			 db.session.commit()
			 return jsonify({'message': 'Symptom updated!'}) 
			 return jsonify({'message': 'Symptom not found!'}), 404 
			 
	@app.route('/history_symptoms', methods=['GET']) 
	def history_symptoms():
		 thirty_days_ago = datetime.utcnow() - timedelta(days=30) 
		 symptoms = Symptom.query.filter(Symptom.timestamp >= thirty_days_ago).all() 
		 return jsonify([{'id': sym.id, 'name': sym.name, 'taken': sym.taken, 'timestamp': sym.timestamp} for sym in symptoms]) 
		 
	if __name == '__main': 
		db.create_all() # Create database tables 
		app.run(debug=True)
