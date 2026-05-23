from flask import Flask, jsonify
import ipl
app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world'

@app.route('/api/teams')
def teams():
    teams = ipl.teamsApi()
    return jsonify(teams)

app.run(debug=True)