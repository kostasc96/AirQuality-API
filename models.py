from model1 import Model1

class Model:
    def __init__(self):
        self.model1 = Model1()

    def updateModel1a(self, acc):
        self.model1.update_model1a(acc)

    def updateModel1b(self, acc):
        self.model1.update_model1b(acc)

    def getModel1a(self):
        return self.model1.get_model1a()

    def getModel1b(self):
        return self.model1.get_model1b()