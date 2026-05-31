from flask import Flask, render_template, url_for
from routes.iblog import iblog_bp

app = Flask(__name__)

app.register_blueprint(iblog_bp)

@app.route('/')
def home():
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)