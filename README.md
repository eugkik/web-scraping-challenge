# web-scraping-challenge

The mission_to_mars.ipynb Jupyter Notebook scrapes various data from four different websites using Splinter, BeautifulSoup, and Pandas.

The Jupyter Notebook was exported as a Python script and modified to store the scraped data into a Python dictionary.  A Scrape function returns the dictionary when called.

The app.py Flask file has two routes:

- The /scrape route calls the Scrape function and stores the returned data into a Mondo database as a Python dictionary.
- The / root route queries the Mongo database and passes the data into an HTML template to display the data on a web page.