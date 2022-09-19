from flask import jsonify, request
from flask import Blueprint
from initiators import model, scalers, prediction, meteo
from util import utils
import numpy as np
import pandas as pd

route1 = Blueprint('route1', __name__)


@route1.route('/model1a')
def model1a():
    req = request.get_json()
    tmpDs = meteo.update_meteo_value(req['station_id'], req['val'])
    pred = model.get_model("1a").predict(tmpDs)
    preds = scalers.get_scaler(True, "b").inverse_transform(pred.reshape(-1, 1)).reshape(pred.shape)
    return_list = []
    for l in preds[0]:
        return_list.append(utils["pm10_index"](l[0]))
    prediction.update_station_pred(req['station_id'], return_list)
    return jsonify(prediction.get_prediction(req['station_id']))


@route1.route('/model1b', methods = ['POST'])
def model1b():
    req = request.get_json()
    tmpDs = np.array(meteo.update_meteo_value(req['station_id'], req['val']))
    # tmpDs = pd.DataFrame({'station_id': tmpDs[:, 0], 'date_time': tmpDs[:, 1], 'forecast_tempC': tmpDs[:, 2], 'forecast_humidity': tmpDs[:, 3], 'forecast_windSpeed': tmpDs[:, 4], 'forecast_windDirection': tmpDs[:, 5], 'pm10': tmpDs[:, 6]})
    cnt = 0
    for i in tmpDs[0]:
        j = np.array([[i[2], i[3], i[4], i[5], i[6]]])
        j = scalers.get_scaler(False, "a").transform(j)
        tmpDs[0][cnt] = [i[0], i[1], j[0][0], j[0][1], j[0][2], j[0][3], j[0][4]]
        cnt = cnt + 1
    print(tmpDs)
    pred = model.get_model("1b").predict(tmpDs)
    preds = scalers.get_scaler(False, "b").inverse_transform(pred.reshape(-1, 1)).reshape(pred.shape)
    return_list = []
    for l in preds[0]:
        return_list.append(utils["pm10_index"](l[0]))
    prediction.update_station_pred(req['station_id'], return_list)
    return jsonify(prediction.get_prediction(req['station_id']))


@route1.route('/model2a')
def model2a():
    return jsonify(2)


@route1.route('/model2b')
def model2b():
    return jsonify(2)
