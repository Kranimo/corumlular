from flask import Flask, send_from_directory, render_template_string

app = Flask(__name__)

@app.route('/')
def welcome():
    # Serve the welcome.html page directly from string or file
    welcome_html = """
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8" />
        <title>Hoşgeldin</title>
    </head>
    <body>
        <h2>Hoşgeldin</h2>
        <h4>Buraya tıkla</h4>
        <p><a href="/main">Fotoğraflar sayfasına git</a></p>
    </body>
    </html>
    """
    return render_template_string(welcome_html)

@app.route('/main')
def main_page():
    return send_from_directory('.', 'main.html')

@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('images', filename)

if __name__ == "__main__":
    app.run(debug=True)
