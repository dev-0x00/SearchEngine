
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
        dataSet = []
        for link in data:
            name = link.split(" ")[0].split("/")[3]
            gmail = link.split(" ")[2]
            link = link.split(" ")[0]
            details = search.GetLinkTree(link.split(" ")[0])
            if len(gmail.split("@")) == 1:
                pass

            else:
                dataDict = {
                    "Name"   : name,
                    "Email"  : gmail,
                    "Link"   : link,
                    "Details": details
                } 
                dataSet.append(dataDict)

        return render_template("index.html", listData=dataSet)
    
    if request.method == "GET":
        return render_template('index.html')
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)