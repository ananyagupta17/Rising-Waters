from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # change if your main page is different

@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/high')
def high():
    return render_template('high.html')

@app.route('/mid')
def moderate():
    return render_template('mid.html')  # assuming 'mid.html' is for moderate

@app.route('/low')
def low():
    return render_template('low.html')

if __name__ == '__main__':
    app.run(debug=True)
