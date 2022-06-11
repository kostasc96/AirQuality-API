import subprocess
import sys

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Flask==2.0.0'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Werkzeug==2.0.0'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'jinja2==3.0.3'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'scikit-learn==1.0.2'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'keras==2.8.0'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tensorflow==2.8.0'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'cassandra-driver==3.25.0'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'joblib'])

from flask import Flask
from routes.PredictionRoutes import route1
from routes.TrainingRoutes import route2

app = Flask(__name__)
app.register_blueprint(route1, url_prefix="/api/prediction")
app.register_blueprint(route2, url_prefix="/api/training")

if __name__ == '__main__':
    app.run()
