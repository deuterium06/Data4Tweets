from flask import Flask, render_template, request, make_response, jsonify
from Data4Tweets.tweets.trendingpokemon import TrendingPokemon

app = Flask(__name__, template_folder='frontend/templateFiles', static_folder='frontend/staticFiles')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        name = request.form['name']
        pokeCount = TrendingPokemon(name).countPokemon()

        if pokeCount < 0:
            generate = f"It's not a pokemon name. Pls try another. :("
        else:
            generate = f"There are {pokeCount} tweets for {name} in the past 7 days!"
        return render_template('index.html', generate=generate)
    else:
        return render_template('index.html')

#error handling
@app.errorhandler(404)
def not_found(error):
    return make_response("Error: Not found!", 404)

@app.errorhandler(400)
def not_found(error):
    return make_response("Error: Bad request!", 400)

if __name__ == '__main__':
    app.run(debug = True)