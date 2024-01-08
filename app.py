from flask import Flask, render_template, request
from main import predict
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        area = int(request.form['area'])
        int_sqft = int(request.form['int_sqft'])
        dist_mainroad = int(request.form['dist_mainroad'])
        n_bedroom = int(request.form['n_bedroom'])
        n_bathroom = int(request.form['n_bathroom'])
        n_room = int(request.form['n_room'])
        park_facil = int(request.form['park_facil'])
        result = predict(area , int_sqft ,dist_mainroad,n_bedroom ,n_bathroom ,n_room,park_facil)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
