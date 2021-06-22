from flask import Flask, render_template
from phrasal_verb import definition, generated_verb
from burgeramt import dialogue_part1, dialogue_part2, dialogue_part3, dialogue_part4,dialogue_part5,dialogue_part6,dialogue_part7


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

@app.route('/burgeramt')
def burgeramt():
    return render_template("burgeramt.html", data= {
        "part1":dialogue_part1(),
        "part2":dialogue_part2(),
        "part3":dialogue_part3(),
        "part4":dialogue_part4(),
        "part5":dialogue_part5(),
        #"part6":dialogue_part6()
        "part7":dialogue_part7()
        }
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = '8000', debug = True)
