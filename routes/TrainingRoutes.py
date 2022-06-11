from flask import jsonify, Response
from flask import Blueprint
from clients.cassandra import get_cassandra_client

session = get_cassandra_client('localhost', 9042, 'airquality')

route2 = Blueprint('route2', __name__)


@route2.route('/online')
async def online_training():
    return jsonify({"result":"connection successful"})
