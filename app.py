from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Simple Flask Web App version 2.0 </h1>"

@app.route('/about')
def about():
    return "<p>This is a simple Flask application to demonstrate a basic web server setup.</p>"

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name', 'Guest')
        return f"<h2>Hello, {name}!</h2>"
    return '''
        <form method="POST">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name">
            <button type="submit">Greet Me</button>
        </form>
    '''
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
