from flask import jsonify, Response
from flask import Blueprint
from flask import request



route1 = Blueprint('route1', __name__)


@route1.route('/model1a')
def model1():
    return jsonify(1)


@route1.route('/model1b')
def model1():
    return jsonify(1)



@route1.route('/model2a')
def model2():
    return jsonify(2)


@route1.route('/model2b')
def model2():
    return jsonify(2)



@route1.route('/model3a')
def model3():
    return jsonify(3)


@route1.route('/model3b')
def model3():
    return jsonify(3)