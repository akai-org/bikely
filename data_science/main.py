from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import json
import joblib

app = Flask(__name__)


def predict_cons(df: pd.DataFrame):
    fuel_one_hot = joblib.load('joblib/fuel_one_hot.joblib')
    producer_one_hot = joblib.load('joblib/producer_one_hot.joblib')
    vehicle_class_one_hot = joblib.load('joblib/vehicle_class_one_hot.joblib')
    transmission_one_hot = joblib.load('joblib/transmission_one_hot.joblib')
    
    fuel_predictor = joblib.load('joblib/fuel_estimator.joblib')

    fuel_type = fuel_one_hot.transform(df[['fuel_type']])
    producer = producer_one_hot.transform(df[['producer']])
    vehicle_class = vehicle_class_one_hot.transform(df[['vehicle_class']])
    transmission_type = transmission_one_hot.transform(df[['transmission_type']])

    X = np.concatenate([producer, vehicle_class, fuel_type, transmission_type, df[['engine_size', 'gears']]], axis=1)
    pred_y = fuel_predictor.predict(X)

    return pred_y


def predict_co2(df: pd.DataFrame):
    fuel_one_hot = joblib.load('joblib/fuel_one_hot.joblib')

    co2_predictor = joblib.load('joblib/co2_estimator.joblib')

    fuel_type = fuel_one_hot.transform(df[['fuel_type']])
    X =  np.concatenate([fuel_type, df[['fuel_cons']]], axis=1)
    pred_y = co2_predictor.predict(X)

    return pred_y


@app.route("/predict", methods=['POST'])
def predict():
    data = json.loads(request.data)
    data = {i: [data[i]] for i in data}
    df = pd.DataFrame.from_dict(data)

    if np.all(df.fuel_cons.isna()):
        fuel_cons = predict_cons(df)
        df['fuel_cons'] = fuel_cons
    
    co2 = predict_co2(df)

    return jsonify({'co2': co2[0]})


@app.route('/producer', methods=['GET'])
def get_producers():
    producer_one_hot = joblib.load('joblib/producer_one_hot.joblib')

    return jsonify(list(producer_one_hot.categories_[0]))


@app.route('/fuel', methods=['GET'])
def get_fuels():
    fuel_one_hot = joblib.load('joblib/fuel_one_hot.joblib')

    return jsonify(list(fuel_one_hot.categories_[0]))


@app.route('/transmission', methods=['GET'])
def get_transmission():
    transmission_one_hot = joblib.load('joblib/transmission_one_hot.joblib')

    return jsonify(list(transmission_one_hot.categories_[0]))


@app.route('/vehicle_class', methods=['GET'])
def get_vehicle_class():
    vehicle_one_hot = joblib.load('joblib/vehicle_class_one_hot.joblib')

    return jsonify(list(vehicle_one_hot.categories_[0]))

@app.route('/personal_median', methods=['GET'])
def get_personal_median():
    median_json = open('joblib/median.json')
    personal_median = json.load(median_json)['personal']
    return jsonify(personal_median)

@app.route('/cargo_median', methods=['GET'])
def get_cargo_median():
    median_json = open('joblib/median.json')
    cargo_median = json.load(median_json)['cargo']
    return jsonify(cargo_median)

if __name__ == '__main__':
    app.run(debug=True)
