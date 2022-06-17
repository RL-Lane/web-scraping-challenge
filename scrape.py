from bs4 import BeautifulSoup as bs
import requests
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
import pandas as pd
import requests
import time



def scrape():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Step 1 - Scraping
    # NASA Mars News
    url = "https://redplanetscience.com/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    news_title = soup.find_all('div', class_="content_title")
    first_news_title = news_title[0].text
    ## first_news_title

    news_paragraph = soup.find_all('div', class_="article_teaser_body")
    first_news_paragraph = news_paragraph[0].text
    ## first_news_paragraph


    # JPL Mars Space Images - Featured Image
    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    featured_image_url = browser.links.find_by_partial_href('image/featured')['href']
    ## featured_image_url

    # Mars Facts
    url = "https://galaxyfacts-mars.com/"
    header = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}
    r = requests.get(url, headers=header)
    
    tables = pd.read_html(r.content)

    mars_facts = tables[1].to_html(header=False, index=False, classes='table table-striped')
    ## mars_facts

    # Mars Hemispheres
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    time.sleep(1)
    links = browser.links.find_by_partial_text('Hemisphere')
    hemi_urls = []
    [hemi_urls.append(links[i]['href']) for i in range(len(links))]
    # Parse image title and hq img url from each page:
    hemisphere_image_urls = []
    for i in range(len(hemi_urls)):
        url = hemi_urls[i]
        browser.visit(url)
        # load image url
        link = browser.links.find_by_partial_text('Sample')[0]['href']
        
        # locate title within page
        html = browser.html
        soup = bs(html, 'html.parser')
        title = soup.find('h2', class_='title').text
        
        # append into list
        hemisphere_image_urls.append({
            'title': title,
            'img_url': link
        })
    ## hemisphere_image_urls

    # load all variables into dictionary
    scraped = {
        'news': {
            'first_title': first_news_title,
            'first_paragraph': first_news_paragraph
        },
        'featured_image_url': featured_image_url,
        'mars_facts':mars_facts,
        'hemisphere_images_urls':hemisphere_image_urls
    }

    browser.quit()
    return scraped
