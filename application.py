from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('home.html')

@app.route('/intro')
def introPage():
    return render_template('intro.html')

@app.route('/experience')
def expPage():
    return render_template('exp.html')

@app.route('/contact')
def contactPage():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()