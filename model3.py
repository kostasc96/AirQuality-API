from keras.models import load_model


class Model3:
    def __init__(self):
        self.model3a = load_model("models3/model1.h5")
        self.model3b = load_model("models3/model2.h5")
        self.accuracy_model3a = 60
        self.accuracy_model3b = 60

    def update_model3a(self, acc):
        self.accuracy_model3a = acc
        self.model3a = load_model("models3/model1.h5")


    def update_model3b(self, acc):
        self.accuracy_model3b = acc
        self.model3b = load_model("models3/model2.h5")


    def get_model3a(self):
        return self.model3a

    def get_model3b(self):
        return self.model3b

    def get_accuracy_model3a(self):
        return self.accuracy_model3a

    def get_accuracy_model3b(self):
        return self.accuracy_model3a