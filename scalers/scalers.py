import joblib


class ScalerDNN:
    def __init__(self, base_path):
        self.scaler1a = joblib.load(f'{base_path}/scaler1a.gz')
        self.scaler1b = joblib.load(f'{base_path}/scaler1b.gz')
        self.scaler3a = joblib.load(f'{base_path}/scaler3a.gz')
        self.scaler3b = joblib.load(f'{base_path}/scaler3b.gz')

    def get_scaler(self, ver):
        scaler_fn = self.get_scalers(ver)
        return scaler_fn

    def get_scalers(self, ver):
        if ver == "1a":
            return self._get_scaler_1a()
        elif ver == "1b":
            return self._get_scaler_1b()
        elif ver == "3a":
            return self._get_scaler_3a()
        else:
            return self._get_scaler_3b()

    def _get_scaler_1a(self):
        return self.scaler1a

    def _get_scaler_1b(self):
        return self.scaler1b

    def _get_scaler_3a(self):
        return self.scaler3a

    def _get_scaler_3b(self):
        return self.scaler3b
