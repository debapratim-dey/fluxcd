import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>My first flux-cd trial</h1><p>This is an updated image.</p>"

app.run()