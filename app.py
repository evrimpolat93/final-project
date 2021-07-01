# Importing essential libraries
from flask import Flask, render_template
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'heart_attack_prediction_rfc_model.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/predictions')
def predictions():
     if request.method == 'POST':
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['chest_pain'])
        tr = int(request.form['blood_pressure'])
        chol = int(request.form['cholestoral'])
        fbs = int(request.form['blood_sugar'])
        ecg = int(request.form['cardiographic_results'])
        chh = int(request.form['heart_rate'])
        exng = int(request.form['angina'])
        peak = float(request.form['previous_peak'])

        data = np.array([[age, sex, cp, tr, chol, fbs, ecg, chh, exng, peak]])
        prediction = classifier.predictions(data)
        
        return render_template('result.html', prediction=prediction)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':

    # Run this when running on LOCAL server...
    app.run(debug=True)

    # ...OR run this when PRODUCTION server.
    # app.run(debug=False)