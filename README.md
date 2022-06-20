# web-scraping-challenge

## Robert Lane

### Background

The purpose of this project is to demonstrate the ability to scrape data through a process known as ETL - Extract, Transform, & Load.  In this project, the following webpages are used as data sources:  
* https://redplanetscience.com/
* https://spaceimages-mars.com/ 
* https://galaxyfacts-mars.com/
* https://marshemispheres.com/

The code to scrape this data was developed using Jupyter Notebook, Pandas, and python.  After testing the code, it was modified to run within a python-native application.

### Prerequisites to run

python packages:
	* Beautiful Soup 4  
	* webdriver_manager  
	* splinter  
	* pandas
MongoDB

### Challenges

* Some webpages require a user-agent string (which helps the website know which kind of browser and operating system is requesting the page).  One was to provide this is copying a user-agent string from a browser into the code, then including that in the requests.get() function.  Another method is to implement splinter and let an actual browser handle the request.  Both methods are implemented within this project.

* When running pandas.read_html on the data provided by the requests.get() function, Incorrectly decoded characters were found.  As it turns out, the issue stems from a character encoding issue.  

	* On line 45 of scrape.py, the code uses "r.content" .  This provides a data stream which is correctly interpreted as unicode characters.  Previously, it was "r.text" , which stored data as [ISO-8859-1](https://stackoverflow.com/questions/44203397/python-requests-get-returns-improperly-decoded-text-instead-of-utf-8).  Although this link provides a different solution, this ended up being a simpler solution to the problem.

### How To Run

	* Ensure prequisites are fulfilled.

	* Open a GIT Bash or terminal window in the root folder of this folder, type "python app.py" and press Enter.

	* Open MongoDB if it isn't running.

	* Open a browser window to [this location](localhost:5000).

To refresh the information, simply click the "Scrape" button.  It may take up to a minute for the browser configuration to fully load prior to execution of the code.  Subsequent scraping attempts in the same session should have reduced loading times.