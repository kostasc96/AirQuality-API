from flask import jsonify, Response
from flask import Blueprint
from flask import request


route2 = Blueprint('route2', __name__)



@route2.route('/online')
def online_training():
    return jsonify(4)