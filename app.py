from flask import Flask

app = Flask(name)

@app.route("/")
def home():
    return """
    <h1>My First App</h1>
    <p>Hello World!</p>
    <button onclick="alert('Hello!')">Click Me</button>
