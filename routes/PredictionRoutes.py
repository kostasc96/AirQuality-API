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


# @route1.route('/model1b', methods=['POST'])
# def model1b():
#     req = request.get_json()
#     tmpDs = np.array(meteo.update_meteo_value(req['station_id'], req['val']))
#     tmpDs = tmpDs[0]
#     df = pd.DataFrame({'station_id': tmpDs[:, 0], 'date_time': tmpDs[:, 1], 'forecast_tempC': tmpDs[:, 2],
#                        'forecast_humidity': tmpDs[:, 3], 'forecast_windSpeed': tmpDs[:, 4],
#                        'forecast_windDirection': tmpDs[:, 5], 'pm10': tmpDs[:, 6]})
#     df['date_time'] = df['date_time'].astype("|S")
#     df['date_time'] = df['date_time'].astype(int)
#     df['forecast_windDirection'] = df['forecast_windDirection'].astype(np.float64)
#     df['station_id'] = df['station_id'].astype(int)
#     df[['forecast_tempC', 'forecast_humidity', 'forecast_windSpeed', 'forecast_windDirection',
#         'pm10']] = scalers.get_scaler(False, "a").fit_transform(
#         df[['forecast_tempC', 'forecast_humidity', 'forecast_windSpeed', 'forecast_windDirection', 'pm10']])
#     df = df.append(df.tail(1))
#     df_pred = utils["create_x"](df[['station_id','date_time','forecast_tempC','forecast_humidity','forecast_windSpeed','forecast_windDirection','pm10']], 72)
#     df_pred = np.array(df_pred)
#     preds = model.get_model("1b").predict(df_pred)
#     return_list = []
#     for l in preds[0]:
#         return_list.append(utils["pm10_index"](l[0]))
#     prediction.update_station_pred(req['station_id'], return_list)
#     return jsonify(prediction.get_prediction(req['station_id']))


@route1.route('/model1b', methods=['POST'])
def model1b():
    req = request.get_json()
    req_val = req["val"]
    station_id = req["station_id"]
    df = pd.read_csv("routes/NeaSmirni.csv", sep=',', header=True)
    df = df[['station_id','date_time','forecast_tempC','forecast_humidity','forecast_windSpeed','forecast_windDirection','pm10']]
    new_row = {'station_id': req[0], 'date_time': req[1], 'forecast_tempC': req[2],
                        'forecast_humidity': req[3], 'forecast_windSpeed': req[4],
                        'forecast_windDirection': req[5], 'pm10': req[6]}
    df = df.append(new_row, ignore_index=True)

    # tmpDs = np.array(meteo.update_meteo_value(req['station_id'], req['val']))
    # tmpDs = tmpDs[0]
    # df = pd.DataFrame({'station_id': tmpDs[:, 0], 'date_time': tmpDs[:, 1], 'forecast_tempC': tmpDs[:, 2],
    #                    'forecast_humidity': tmpDs[:, 3], 'forecast_windSpeed': tmpDs[:, 4],
    #                    'forecast_windDirection': tmpDs[:, 5], 'pm10': tmpDs[:, 6]})
    df['date_time'] = df['date_time'].astype("|S")
    df['date_time'] = df['date_time'].map(lambda a: utils["get_time"](a))
    df['date_time'] = df['date_time'].astype(int)
    df['forecast_windDirection'] = df['forecast_windDirection'].astype(np.float64)
    df['station_id'] = df['station_id'].astype(int)
    df[['forecast_tempC', 'forecast_humidity', 'forecast_windSpeed', 'forecast_windDirection',
        'pm10']] = scalers.get_scaler(False, "a").fit_transform(
        df[['forecast_tempC', 'forecast_humidity', 'forecast_windSpeed', 'forecast_windDirection', 'pm10']])
    # df = df.append(df.tail(1))
    df_pred = utils["create_x"](df[['station_id','date_time','forecast_tempC','forecast_humidity','forecast_windSpeed','forecast_windDirection','pm10']], 72)
    # df_pred = np.array(df_pred)
    df_pred = pd.DataFrame(df_pred, columns=['station_id','date_time','forecast_tempC','forecast_humidity','forecast_windSpeed','forecast_windDirection','pm10'])
    preds = model.get_model("1b").predict(df_pred)
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
