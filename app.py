from flask import *
import pickle
import pandas as pd

app = Flask(__name__)

def load_status_predictor():
    with open('xgb_status.pkl', 'rb') as file:
        model = pickle.load(file)

    return model

def load_top500_predictor():
    with open('xgb_top500.pkl', 'rb') as file:
        model = pickle.load(file)

    return model

status_predictor = load_status_predictor()
top500_predictor = load_top500_predictor()

@app.route('/')
def home():
    return 'I <3 ADVAY VYAS!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    df = pd.DataFrame(data, index=[0])

    status_predictions = status_predictor.predict(data)
    top500_predictions = top500_predictor.predict(data)

    return jsonify({'status_predictions': status_predictions.tolist(), 'top500_prediction': top500_predictions.tolist()})

if __name__ == '__main__':
    app.run(debug=True)