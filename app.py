from flask import Flask, render_template, url_for
from routes.iblog import iblog_bp
from routes.inews import inews_bp
from routes.isongs import isong_bp

app = Flask(__name__)

app.register_blueprint(iblog_bp)
app.register_blueprint(inews_bp)
app.register_blueprint(isong_bp)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)