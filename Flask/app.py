from flask import Flask, url_for, jsonify, request, json

import pickle
import numpy as np

with open("modelo_xgboost.pkl", "rb") as f:
        model = pickle.load(f)

app = Flask(__name__)

@app.route('/', methods=['POST']) 
def predict(): 
	if request.headers['Content-Type'] == 'application/json':
		input=request.json['input']
	results = {} 
	y_hat = model.predict(np.array(input))
	results['parameters']= input
	results['resultado'] = y_hat.tolist() 
	return jsonify(results)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
