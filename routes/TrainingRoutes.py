from flask import jsonify, Response
from flask import Blueprint
from clients.cassandra import get_cassandra_client
import time
import threading
from sklearn.model_selection import train_test_split
import pandas as pd
from numpy import float64
from apscheduler.schedulers.background import BackgroundScheduler
from util import utils
from initiators import scalers, window, horizon, model, epochs, batch_size

session = get_cassandra_client('localhost', 9042, 'airquality')

route2 = Blueprint('route2', __name__)


def pandas_factory(colnames, rows):
    return pd.DataFrame(rows, columns=colnames)


# def sensor():
#     session.row_factory = pandas_factory
#     session.default_fetch_size = 10000
#     query = """ """
#     rows = session.execute(query)
#     df = rows._current_rows
#     df['date_time'] = df['date_time'].astype("|S")
#     df['season'] = df['season'].astype("|S")
#     df['date_time'] = df['date_time'].map(lambda a: utils["get_time"](a))
#     df['date_time'] = df['date_time'].astype(int)
#     df['season'] = df['season'].map(lambda a: utils["get_season"](a))
#     df['season'] = df['season'].astype(float64)
#     df['forecast_windDirection'] = df['forecast_windDirection'].astype(float64)
#     df['station_id'] = df['station_id'].astype(int)
#     df2 = df[['pm10']]
#     df[['forecast_tempC', 'forecast_humidity', 'forecast_windSpeed', 'forecast_windDirection','pm10']] = scalers._get_scaler_1a().fit_transform(df[['forecast_tempC', 'forecast_humidity', 'forecast_windSpeed', 'forecast_windDirection', 'pm10']])
#     df2 = scalers._get_scaler_1b().fit_transform(df2.values)
#     X, y = utils["create_xy"](df[['station_id', 'date_time', 'forecast_tempC', 'forecast_humidity', 'forecast_windSpeed','forecast_windDirection', 'pm10']], df2, window, horizon)
#     m = model.get_model("3a")
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
#     model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)
#     predictions = model.predict(X_test)
#     predictions = scalers._get_scaler_1b().inverse_transform(predictions.reshape(-1, 1)).reshape(predictions.shape)
#     y_test = scalers._get_scaler_1b().inverse_transform(y_test.reshape(-1, 1)).reshape(y_test.shape)
#     predictions, y_test = utils["convert_pm10_index"](predictions, y_test)
#     current_acc = m.get_accuracy_models("3a")
#     new_acc = utils["calc_pm10_accuracy"](predictions, y_test, 48)
#     m.save("models3/model1.h5")
#     if new_acc >= current_acc:
#         m.save('models2/model1.h5')
#     print("Scheduler is alive!")
#
#
# sched = BackgroundScheduler(daemon=True)
# sched.add_job(sensor, 'interval', seconds=5)
# sched.start()


@route2.route('/online')
async def online_training():
    def thread_function(value, con, models):
        print("Thread %s: starting" + str(value))
        time.sleep(value)
        print(models.get_accuracy_models("1a"))
        print("Thread %s: finishing" + str(value))

    thread = threading.Thread(target=thread_function, kwargs={'value': 20, 'con': session, 'models': model})
    thread.start()
    return jsonify({"result": "connection successful"})
