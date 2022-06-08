from keras.models import load_model


class Model1:
    def __init__(self):
        self.model1a = load_model("models/model1.h5")
        self.model1b = load_model("models/model2.h5")

    def update_model1a(self):
        self.model1a = load_model("models/model1.h5")


    def update_model1b(self):
        self.model1b = load_model("models/model2.h5")


    def get_model1a(self):
        return self.model1a

    def get_model1b(self):
        return self.model1b