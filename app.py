# 1. import Flask
from flask import Flask, render_template, redirect
import scrape
from flask_pymongo import PyMongo




# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/marsDB")

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars = mars)



@app.route("/scrape")
def scraper():
    

     # Run the scrape function
    mars = scrape.scrape()

    # Insert the record
    mongo.db.mars.update_one({}, {"$set": mars}, upsert=True)
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)


# datum = {
#     'news': scrapes[0]['news'],
#     'featured_image_url': scrapes[0]['featured_image_url'],
#     'mars_facts': scrapes[0]['mars_facts'],
#     'hemisphere_images_urls': scrapes[0]['hemisphere_images_urls']
# }