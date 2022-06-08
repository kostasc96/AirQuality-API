from keras.models import load_model


class Model1:
    def __init__(self):
        self.model1a = load_model("models/model1.h5")
        self.model1b = load_model("models/model2.h5")
        self.accuracy_model1a = 60
        self.accuracy_model1b = 60

    def update_model1a(self, acc):
        self.accuracy_model1a = acc
        self.model1a = load_model("models/model1.h5")

    def update_model1b(self, acc):
        self.accuracy_model1b = acc
        self.model1b = load_model("models/model2.h5")

    def get_model1a(self):
        return self.model1a

    def get_model1b(self):
        return self.model1b

    def get_accuracy_model1a(self):
        return self.accuracy_model1a

    def get_accuracy_model1b(self):
        return self.accuracy_model1a
