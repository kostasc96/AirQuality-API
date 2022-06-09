from models import ModelAirQuality
from scalers.scalers import ScalerDNN
from predictions import Prediction


model = ModelAirQuality(60)
scalers = ScalerDNN("scalers")
prediction = Prediction()