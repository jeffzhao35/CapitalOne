from flask import Flask, render_template, request, redirect, url_for
from api_client import ApiClient
import pdb
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		park_name = request.form['park_name']
		state = request.form['state']
		return redirect(url_for('results', state=state))
	else:
		return render_template("index.html")


@app.route('/results', methods=['GET'])
def results():
	state = request.args.get('state')
	parks = ApiClient.parks(state=state)
	return render_template("results.html", parks=parks)
