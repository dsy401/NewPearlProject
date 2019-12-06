from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('pages/Home/Home.html')


if __name__ == '__main__':
    # app.run(threaded=True,port=5000)

    from waitress import serve
    serve(app,host='localhost',port=8080)