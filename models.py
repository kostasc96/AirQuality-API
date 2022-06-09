from base_model import BaseModel


class Model:
    def __init__(self):
        self.model1 = BaseModel("models")
        self.model2 = BaseModel("models2")
        self.model3 = BaseModel("models3")

    def get_model(self, model_ver):
        model = self.get_model_ver(model_ver)
        return model

    def get_model_ver(self, model_ver):
        if model_ver == "1a":
            return self._get_model1a()
        elif model_ver == "1b":
            return self._get_model1b()
        elif model_ver == "2a":
            return self._get_model2a()
        elif model_ver == "2b":
            return self._get_model2b()
        elif model_ver == "3a":
            return self._get_model3a()
        elif model_ver == "3b":
            return self._get_model3b()

    def _get_model1a(self):
        return self.model1.get_model_a()

    def _get_model1b(self):
        return self.model1.get_model_b()

    def get_accuracy_1a(self):
        return self.model1.get_accuracy_model_a()

    def get_accuracy_1b(self):
        return self.model1.get_accuracy_model_b()

    def _get_model2a(self):
        return self.model2.get_model_a()

    def _get_model2b(self):
        return self.model2.get_model_b()

    def update_model2a(self, acc):
        self.model2 = self.model2.update_model_a(acc)

    def update_model2b(self, acc):
        self.model2 = self.model2.update_model_b(acc)

    def get_accuracy_2a(self):
        return self.model2.get_accuracy_model_a()

    def get_accuracy_2b(self):
        return self.model2.get_accuracy_model_b()

    def _get_model3a(self):
        return self.model3.get_model_a()

    def _get_model3b(self):
        return self.model3.get_model_b()

    def update_model3a(self, acc):
        self.model3 = self.model3.update_model_a(acc)

    def update_model3b(self, acc):
        self.model3 = self.model3.update_model_b(acc)

    def get_accuracy_3a(self):
        return self.model3.get_accuracy_model_a()

    def get_accuracy_3b(self):
        return self.model3.get_accuracy_model_b()
