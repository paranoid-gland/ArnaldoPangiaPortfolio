from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def bio():
    return render_template("about.html")

@app.route('/test')
def test():
    return render_template("test.html")
    
@app.route('/seagull')
def seagull():
    return render_template("seagull.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = '8000', debug = True)
