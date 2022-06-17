from flask import Flask, render_template
from datetime import date

#year variable for copyright statement so I can be lazy and not update it
year = date.today().year

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', year=year)


if __name__ == "__main__":
    app.run(debug=True)