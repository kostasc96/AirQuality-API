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
