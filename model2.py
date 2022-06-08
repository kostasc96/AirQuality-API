from keras.models import load_model


class Model2:
    def __init__(self):
        self.model2a = load_model("models2/model1.h5")
        self.model2b = load_model("models2/model2.h5")
        self.accuracy_model2a = 60
        self.accuracy_model2b = 60

    def update_model2a(self, acc):
        self.accuracy_model2a = acc
        self.model2a = load_model("models2/model1.h5")


    def update_model2b(self, acc):
        self.accuracy_model2b = acc
        self.model2b = load_model("models2/model2.h5")


    def get_model2a(self):
        return self.model2a

    def get_model2b(self):
        return self.model2b

    def get_accuracy_model2a(self):
        return self.accuracy_model2a

    def get_accuracy_model2b(self):
        return self.accuracy_model2a