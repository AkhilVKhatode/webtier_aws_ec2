import os
import csv
from flask import Flask, request
from gunicorn.app.base import BaseApplication

app = Flask(__name__)

def load_results(csv_file):
    results = {}
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            filename, prediction = row
            results[filename] = prediction
    return results

def predict_results(image_filename, prediction_results):
    image_filename = os.path.splitext(image_filename)[0]
    prediction = prediction_results.get(image_filename)
    if prediction is None:
        return "Unknown"
    return prediction

@app.route("/", methods=["POST"])
def handle_request():
    predictions = {}
    
    if 'inputFile' not in request.files:
        return "No input file provided", 400
    
    files = request.files.getlist('inputFile')
    
    for file in files:
        if file.filename == '':
            continue
        prediction = predict_results(file.filename, app.config['prediction_results'])
        predictions[file.filename.split('.')[0]] = prediction
    response = '\n'.join([f"{filename}:{prediction}" for filename, prediction in predictions.items()])
    
    return response, 200

prediction_file = "Classification Results on Face Dataset (1000 images).csv"
classification_results = load_results(prediction_file)
app.config['prediction_results'] = classification_results

class FlaskApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        for key, value in self.options.items():
            if key in self.cfg.settings and value is not None:
                self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

if __name__ == "__main__":
    gunicorn_options = {
        'bind': '0.0.0.0:5000',
        'workers': 4
    }

    FlaskApplication(app, gunicorn_options).run()
