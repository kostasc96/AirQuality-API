from model1 import Model1
from model2 import Model2
from model3 import Model3


class Model:
    def __init__(self):
        self.model1 = Model1()
        self.model2 = Model2()
        self.model3 = Model3()

    def get_model1a(self):
        return self.model1.get_model1a()

    def get_model1b(self):
        return self.model1.get_model1b()

    def get_model2a(self):
        return self.model2.get_model2a()

    def get_model2b(self):
        return self.model2.get_model2b()

    def update_model2a(self, acc):
        self.model2.update_model2a(acc)

    def update_model2b(self, acc):
        self.model2.update_model2b(acc)

    def get_model3a(self):
        return self.model3.get_model3a()

    def get_model3b(self):
        return self.model3.get_model3b()

    def update_model3a(self, acc):
        self.model3.update_model3a(acc)

    def update_model3b(self, acc):
        self.model3.update_model3b(acc)
