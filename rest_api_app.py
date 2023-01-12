from flask import Flask, jsonify, request
import ml_model_loader as ml

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

# POST method to collect user data and return model output
@app.route('/model', methods=['POST'])
def post_model():
    data = request.get_json()
    data_name = data['virusName']
    data_list = data['userData']

    model = ml.MlModelLoader(data_name, data_list)
    final_output = model.run_model()

    return jsonify(final_output), 201
