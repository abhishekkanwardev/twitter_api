from flask import Flask
from .utils import fetch_user_profile

app = Flask(__name__)

@app.route("/twitter/profile/<username>")
def twitter_profile_view(username):
    resp = fetch_user_profile(username)
    return resp