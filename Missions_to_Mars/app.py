from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Create mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_mission"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_data = mongo.db.data.find_one()
    return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scraper():
    data = mongo.db.data
    mars_data = scrape_mars.scrape()
    data.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
