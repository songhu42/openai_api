import openai
import config
from flask import Flask, render_template 

openai.api_key = config.API_KEY

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello. Flask..."
    
if __name__ == "__main__":
    app.run()
    
