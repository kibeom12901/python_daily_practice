from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0, 9)

@app.route("/")
def home():
    return '''
    <html>
      <head>
        <title>Higher Lower Game</title>
      </head>
      <body>
        <h1>Guess number between 0 and 9</h1>
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="Welcome Gif">
      </body>
    </html>
    '''

@app.route("/<int:user_guess>")
def compare(user_guess):

    if user_guess < random_number:
        message = f"{user_guess} is too small."
        gif_url = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
    elif user_guess > random_number:
        message = f"{user_guess} is too big."
        gif_url = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
    else:
        message = f"{user_guess} is the answer."
        gif_url = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
    
    return f'''
    <html>
      <head>
        <title>Higher Lower</title>
      </head>
      <body>
        <h1>{message}</h1>
        <img src="{gif_url}" alt="Result Gif">
      </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
