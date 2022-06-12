from models import ModelAirQuality
from scalers.scalers import ScalerDNN
from predictions import Prediction
from meteo_72 import Meteo


model = ModelAirQuality(60)
scalers = ScalerDNN("scalers")
prediction = Prediction()
meteo = Meteo()