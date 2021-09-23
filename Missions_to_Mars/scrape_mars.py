from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd

def scrape():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Create new dictionary to store all scraped data
    mars = {}

    #Open News site with splinter
    news_url = 'https://redplanetscience.com'
    browser.visit(news_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    #Scrape news titles and paragraph text as variables
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    #Add news data to dictionary
    mars['news_title'] = news_title
    mars['news_p'] = news_p

    # Open Featured Image site with splinter
    image_url = 'https://spaceimages-mars.com/'
    browser.visit(image_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Find relative path to image
    relative_path = soup.find('img', class_='headerimage fade-in')['src']

    # Create full path to image
    featured_image_url = image_url+relative_path

    # Add featured image to dictionary
    mars['featured_image_url'] = featured_image_url

    # Use Pandas to scrape Mars Facts table
    facts_url = 'https://galaxyfacts-mars.com/'
    table = pd.read_html(facts_url)[0]
    # Rename columns
    table.rename(columns={0:'Description', 1:'Mars', 2:'Earth'}, inplace = True)
    # Change index
    table.set_index('Description', inplace = True)
    # Convert to html
    mars_table = table.to_html()

    # Add table to dictionary
    mars['mars_table'] = mars_table

    # Scrape High Res Images
    # Set home page as variable
    base_url = 'https://marshemispheres.com/'
    # Create list of hemisphere links to open with splinter
    pages = ['cerberus.html', 'schiaparelli.html', 'syrtis.html', 'valles.html']
    # Create list to hold title and url
    hemisphere_image_urls = []

    # Loop through list of hemisphere pages and scrape Title and Image URL
    for page in pages:
        hemi_page = base_url+page
        browser.visit(hemi_page)
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        title = soup.find('h2', class_='title').text
        downloads = soup.find('div', class_='downloads')
        relative_url = downloads.find('a')['href']
        img_url = base_url+relative_url
        hemisphere_image_urls.append({'title':title, 'img_url':img_url})

    # Add list to dictionary
    mars['hemisphere_image_urls'] = hemisphere_image_urls

    # Quit the browser
    browser.quit()

    return mars