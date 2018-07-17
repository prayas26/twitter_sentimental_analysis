from flask import Flask,render_template,request, url_for, redirect
import string
import random
import os

import twitter_sentiment

req_image = os.path.join('static', 'img')

app=Flask(__name__)

def id_generator(size=5, chars=string.ascii_lowercase + string.digits):
    x = ''.join(random.choice(chars) for _ in range(size))
    return x

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/genid', methods=["POST"])
def id_gen():
	usertext = request.form["usertext"]
	no_tweets = request.form["no_tweets"]
	userId = id_generator()
	twitter_sentiment.checksentiment(userId, usertext, no_tweets)
	return render_template("showid.html", userId=userId)

@app.route('/haveid')
def haveid():
	return render_template("haveid.html")

@app.route('/showgraph', methods=["POST"])
def show():
	userid = request.form["userid"]
	img_name = userid+".png"
	for files in os.walk(req_image):
		if img_name in files[2]:
			img_path = os.path.join(req_image, img_name)
			return render_template("showgraph.html", img_name=img_path)
		else:
			return render_template("noimage.html")

if __name__=='__main__':
	app.run(debug=True)