from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/places")
def places():
	return render_template('places.html')

if __name__ == "__main__":
	app.run()