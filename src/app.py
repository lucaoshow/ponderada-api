from flask import Flask, request
from flask_cors import CORS

# Configuração da API
app = Flask(__name__)
CORS(app)

games = ["The Legend of Zelda: Breath of the Wild", "The Legend of Zelda: Tears of the Kingdom", "Mario Kart 8", "Elden Ring"]


# Rota para retorno da lista de jogos
@app.route('/getGames', methods = ["GET"])
def get_games():
    global games
    return games, 200


# Rota para adicionar jogos à lista
@app.route('/addGames', methods = ["POST"])
def add_games():
    global games
    new_games = request.get_data(True, True).split(", ")
    for game in new_games:
        if game not in games:
            games.append(game)
    
    return "", 201


# Rota para apagar algum jogo da lista
@app.route('/deleteGame', methods = ["DELETE"])
def delete_game():
    global games
    game = request.get_data(True, True)
    if game in games:
        games.remove(game)

    return "", 204


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)