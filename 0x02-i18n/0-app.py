from flask import Flask


app = Flask("__name__")

@app.route('/')
def index():
    """This returns the index page
    """
    return('0-index.html')

if __name__ == "__main__":
    app.run(debug=True)