from flask import jsonify, Response
from flask import Blueprint
from flask import request



route1 = Blueprint('route1', __name__)


@route1.route('/model1a')
def model1a():
    return jsonify(1)


@route1.route('/model1b')
def model1b():
    return jsonify(1)



@route1.route('/model2a')
def model2a():
    return jsonify(2)


@route1.route('/model2b')
def model2b():
    return jsonify(2)



@route1.route('/model3a')
def model3a():
    return jsonify(3)


@route1.route('/model3b')
def model3b():
    return jsonify(3)