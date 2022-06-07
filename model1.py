from keras.models import load_model


model1a = load_model("models/model1.h5")
model1b = load_model("models/model2.h5")

def update_model1a():
    model1a = load_model("models/model1.h5")


def update_model1b():
    model1b = load_model("models/model2.h5")


def get_model1a():
    return model1a

def get_model1b():
    return model1b