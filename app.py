from flask import *
import pickle

app = Flask(__name__)

def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    return model

model = load_model()

@app.route('/predict', methods=['PREDICT'])
def predict():
    data = request.get_json()

    print(data)

if __name__ == '__main__':
    app.run()