from flask import *
import pickle
import pandas as pd

app = Flask(__name__)

def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    return model

model = load_model()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    df = pd.DataFrame(data, index=[0])

    predictions = model.predict(df)

    return jsonify({'predictions': predictions.tolist()})

if __name__ == '__main__':
    app.run(debug=True)