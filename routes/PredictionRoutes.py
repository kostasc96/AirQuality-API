from flask import jsonify, request
from flask import Blueprint
from initiators import model, scalers, prediction, meteo
from util import utils

route1 = Blueprint('route1', __name__)


@route1.route('/model1a')
def model1a():
    return jsonify(1)


@route1.route('/model1b', methods = ['POST'])
def model1b():
    tmpDs = request.get_json()['val']
    tmpDs = meteo.update_meteo_value(3, tmpDs)
    pred = model.get_model("3b").predict(tmpDs)
    preds = scalers.get_scaler(True, "b").inverse_transform(pred.reshape(-1, 1)).reshape(pred.shape)
    return_list = []
    for l in preds[0]:
        return_list.append(utils["pm10_index"](l[0]))
    prediction.update_neasmirni(return_list)
    return jsonify(prediction.get_prediction(3))


@route1.route('/model2a')
def model2a():
    return jsonify(2)


@route1.route('/model2b')
def model2b():
    return jsonify(2)
