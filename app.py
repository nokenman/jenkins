from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    build_number = os.getenv("BUILD_NUMBER", "local")

    return f"""
    <html>
        <body>
            <h1>Hello Jenkins!</h1>
            <p>Build number: {build_number}</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    