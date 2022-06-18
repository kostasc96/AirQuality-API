import numpy as np

utils = {}
util = lambda f: utils.setdefault(f.__name__, f)


@util
def pm10_index(val):
    if val <= 25.0:
        return 0
    elif 26.0 <= val <= 50.0:
        return 1
    elif 51.0 <= val <= 90.0:
        return 2
    elif 91.0 <= val <= 180.0:
        return 3
    else:
        return 4


@util
def update_model2a(model, acc):
    if acc > model.get_accuracy_2a():
        model.update_model2a(acc)


@util
def update_model2b(model, acc):
    if acc > model.get_accuracy_2b():
        model.update_model2b(acc)


@util
def update_model3a(model, acc):
    model.update_model3a(acc)


@util
def update_model3b(model, acc):
    model.update_model3b(acc)


@util
def convert_pm10_index(predicts, test):
    for i in range(len(predicts)):
        for j in range(len(predicts[i])):
            predicts[i][j] = pm10_index(predicts[i][j])
            test[i][j] = pm10_index(test[i][j])


@util
def calc_pm10_accuracy(predicts, test, window):
    tot_val = len(predicts) * window
    tot_comp = 0
    for i in range(len(predicts)):
        for j in range(window):
            if abs(predicts[i][j] - test[i][j]) == 1:
                tot_comp = tot_comp + 0.5
            elif abs(predicts[i][j] == test[i][j]):
                tot_comp = tot_comp + 1
    return (100 * tot_comp) / tot_val


@util
def create_xy(series, series2, window_size, prediction_horizon, shuffle=False):
    x = []
    y = []
    for i in range(0, len(series)):
        if len(series[(i + window_size):(i + window_size + prediction_horizon)]) < prediction_horizon:
            break
        x.append(np.array(series[i:(i + window_size)]))
        y.append(np.array(series2[(i + window_size):(i + window_size + prediction_horizon)]))
    x = np.array(x)
    y = np.array(y)
    return x, y
