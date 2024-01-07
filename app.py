from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        num1 = int(request.form['area'])
        num2 = int(request.form['int_sqft'])
        num3 = int(request.form['dist_mainroad'])
        num4 = int(request.form['n_bedroom'])
        num5 = int(request.form['n_bathroom'])
        num6 = int(request.form['n_room'])
        num7 = int(request.form['park_facil'])
        result = num1 + num2 + num3 + num4 + num5 + num6 + num7
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
