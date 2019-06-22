from flask import Flask, render_template, request, redirect, url_for
from api_client import ApiClient
import pdb
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		park_name = request.form['park_name']
		print(park_name)
		state = request.form['state']
		designation = request.form['designation']
		keyword = request.form['keyword']
		return redirect(url_for('results', park_name=park_name, state=state, designation=designation, keyword=keyword))
	else:
		return render_template("index.html")


@app.route('/results', methods=['GET'])
def results():
	park_name = request.args.get('park_name')
	state = request.args.get('state')
	designation = request.args.get('designation')
	keyword = request.args.get('keyword')
	parks = ApiClient.parks(park_name=park_name, state=state, designation=designation, keyword=keyword)
	return render_template("results.html", parks=parks)

if __name__ == '__main__':
    app.run(debug=True)
