from keras.models import load_model


class BaseModel:
    def __init__(self, model_base_path):
        self.model_a = load_model(f'{model_base_path}/model1.h5')
        self.model_b = load_model(f'{model_base_path}/model2.h5')
        self.accuracy_model_a = 60
        self.accuracy_model_b = 60

    def update_model_a(self, acc, model_path):
        self.accuracy_model_a = acc
        self.model_a = load_model(model_path)
        return self

    def update_model_b(self, acc, model_path):
        self.accuracy_model_b = acc
        self.model_b = load_model(model_path)
        return self

    def get_model_a(self):
        return self.model_a

    def get_model_b(self):
        return self.model_b

    def get_accuracy_model_a(self):
        return self.accuracy_model_a

    def get_accuracy_model_b(self):
        return self.accuracy_model_a
