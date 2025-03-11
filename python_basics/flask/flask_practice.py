from flask import Flask

app = Flask(__name__)

@app.route('/')  # Default homepage
def home():
    return """
    <html>
        <head>
            <title>Welcome to My Flask App</title>
        </head>
        <body>
            <h1>Welcome to Flask!</h1>
            <p>This is a simple web application built with Flask.</p>
            <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fpixabay.com%2Fimages%2Fsearch%2Fwebsite%2F&psig=AOvVaw0Es5x0-yFkLxBlBgm5Y8ds&ust=1741737468804000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCOjE5OrbgIwDFQAAAAAdAAAAABAE" alt="Sample Image">
        </body>
    </html>
    """

def make_bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  
        return f"<b>{result}</b>"  
    return wrapper

@app.route('/user/<name>')  
@make_bold
def greet_user(name):
    return f"Hello, {name}!"

@app.route('/square/<int:number>') 
def square_number(number):
    return f"The square of {number} is {number ** 2}"

if __name__ == '__main__':
    app.run(debug=True)  
