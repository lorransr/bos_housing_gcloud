from flask import Flask, request, json
import pickle

def events(request):
    # carregando modelo
    regressor = pickle.load(open("model/regressor","rb"))
    # parseando request
    body_dict =  request.get_json(force=True)
    data = body_dict['data']

    prediction = regressor.predict(data)


if __name__ == '__main__':
    app = Flask(__name__)
    app.route('/predict', methods=['POST'])(lambda: events(request))
    app.run(debug = True)
