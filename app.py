
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My First App</title>
    </head>
    <body style="font-family: Arial; text-align: center; padding: 50px;">
        <h1>My First App</h1>
        <p>Hello World!</p>
        <button onclick="alert('Hello!')">Click Me</button>
    </body>
    </html>
    """
