from flask import Flask, render_template, request
import numpy as np
import pickle  

app = Flask(__name__)
model = pickle.load(open('models/xgb_model.pkl', 'rb'))  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            features = [
            float(request.form['temp']),
            float(request.form['humidity']),
            float(request.form['cloud_cover']),
            float(request.form['annual_rainfall']),
            float(request.form['rain_janfeb']),
            float(request.form['rain_mar_may']),
            float(request.form['rain_jun_sep']),
            float(request.form['rain_octdec']),
            float(request.form['avg_june']),
            float(request.form['sub'])
        ]
            final_input = np.array([features]).reshape(1, -1)

            probability = model.predict_proba(final_input)[0][1]
            percent = round(probability * 100, 2)  

            print(final_input)
            print(model.predict_proba(final_input))


            if percent <= 50:
                return render_template('low.html', percent=percent)
            elif percent <= 75:
                return render_template('mid.html', percent=percent)
            else:
                return render_template('high.html', percent=percent)

        except Exception as e:
            return f"Error: {e}"
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)

