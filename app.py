from flask import Flask
from routes.PredictionRoutes import route1
from routes.TrainingRoutes import route2

app = Flask(__name__)
app.register_blueprint(route1, url_prefix="/api/prediction")
app.register_blueprint(route2, url_prefix="/api/training")

if __name__ == '__main__':
    app.run()
