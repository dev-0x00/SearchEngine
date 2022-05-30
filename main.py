
from flask import Flask, render_template, request, redirect, url_for, session

from scapper import Search

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        query = request.form.get("query")
        search = Search()
        data = search.GetDataLinks(str(query))
        data = sum(data, [])    
        return render_template("index.html", data=data)
    
    if request.method == "GET":
        return render_template('index.html')
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)