from flask import Flask, render_template
from phrasal_verb import definition, generated_verb


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

@app.route('/phrasal_verb')
def phrasal_verb():
    return render_template("phrasal_verb.html", data= {
        "definition":definition(),
        "verb":generated_verb() 
        }
    )



if __name__ == '__main__':
    app.run(host='0.0.0.0', port = '8000', debug = True)
