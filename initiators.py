from models import ModelAirQuality
from scalers.scalers import ScalerDNN
from predictions import Prediction
from meteo_72 import Meteo


model = ModelAirQuality(60)
scalers = ScalerDNN("scalers")
prediction = Prediction()
meteo = Meteo()
window = 72
horizon = 48
epochs = 2
batch_size = 32