from flask import Flask, render_template, request
from main import predict
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        area = request.form['area']
        int_sqft = request.form['int_sqft']
        dist_mainroad = request.form['dist_mainroad']
        n_bedroom = request.form['n_bedroom']
        n_bathroom = request.form['n_bathroom']
        n_room = request.form['n_room']
        park_facil = request.form['park_facil']
        if area and int_sqft and dist_mainroad and n_bathroom and n_bedroom and n_room:
            result = predict(area , int_sqft ,dist_mainroad,n_bedroom ,n_bathroom ,n_room,park_facil)
            return render_template('index.html', result= int(result))
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
