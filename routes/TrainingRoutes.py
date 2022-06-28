from flask import jsonify, Response
from flask import Blueprint
from clients.cassandra import get_cassandra_client
import time
import threading

session = get_cassandra_client('localhost', 9042, 'airquality')

route2 = Blueprint('route2', __name__)


@route2.route('/online')
async def online_training():
    def thread_function(value):
        print("Thread %s: starting" + str(value))
        time.sleep(value)
        print("Thread %s: finishing" + str(value))
    thread = threading.Thread(target=thread_function, kwargs={'value': 20})
    thread.start()
    return jsonify({"result": "connection successful"})
