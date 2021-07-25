# web

https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f

https://duo.com/decipher/driving-headless-chrome-with-python

https://www.datacamp.com/community/tutorials/learn-build-dash-python
**Dash** is Python framework for building web applications. It built on top of Flask, Plotly.js, React and React Js. It enables you to build dashboards using pure Python. Dash is open source, and its apps run on the web browser.


## requests_html
requests_html serves as an alternative to Selenium and PhantomJS, and provides a clear syntax similar to the awesome requests package\\
http://theautomatic.net/2019/01/19/scraping-data-from-javascript-webpage-python

```python
from requests_html import HTMLSession
session = HTMLSession()
resp = session.get(url)    
resp.html.absolute_links #get absolute links
resp.html.render() #run JavaScript code on webpage
soup = bsoup(resp.html.html, 'lxml')
```        

## get with header
```python
import os
import sys
import json
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bsoup

str_url = 'https://www.vv'

print(f'\n{str_url}')

#*****worked similar to php file_get_contents
# get json
import urllib.request
hdr = {'X-Requested-With': 'XMLHttpRequest'}
req = urllib.request.Request(str_url, headers=hdr)
resp = urllib.request.urlopen(req)
htmltext = resp.read()
data = json.loads(htmltext.decode('utf-8'))
print(data[0])
#****************

#****will only get html after js run
session = HTMLSession()
resp = session.get(str_url, headers=hdr)
resp.html.render() #run JavaScript code on webpage
print(resp.html.html)
#************

soup = bsoup(resp.html.html, 'lxml')
tables = soup.find_all('table')

for tbl in tables:
    tbl_body = tbl.find('tbody')
    rows = tbl_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        vals = [ele.text.strip() for ele in cols]
        print(vals)
```

## wbdriver
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

version = 'old'

if version == 'old':
    #create driver
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('accept="application/json"')
    chrome_options.add_argument('user-agent="Chrome"')
    chrome_options.add_argument('x-requested-with=XMLHttpRequest')
    
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #chrome_options.binary_location = r'C:\Users\usr\AppData\Local\Google\Chrome\Application'
    chrome_driver = r'C:\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)

    urls = ['https://www.vvv', 'https://www.ccc']

    for str_url in urls:
        print(f'\n{str_url}')
        driver.get(str_url)
        #driver.Navigate().GoToUrl(str_url);
        print(driver.page_source)
        sys.exit('finished test')

        #soup = bsoup(driver.page_source,'lxml')
        #tables = soup.find_all('table')
        #table_body = tables[0].find('tbody')

        #rows = table_body.find_all('tr')
        #for row in rows:
        #    cols = row.find_all('td')
        #    vals = [ele.text.strip() for ele in cols]
        #    print(vals)

    #---
    #trs = driver.find_elements_by_xpath('//div[@id="app"]//table//tr')
    #for tr in trs:
    #    tds = tr.find_elements_by_tag_name('td')
    #    print ([td.text for td in tds])
    #elem = driver.find_element_by_id('app')
    #-----

    driver.quit()

elif version == 'new':

    #create driver
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--log-level=3')

    chrome_options.add_argument('accept="application/json, text/javascript, */*; q=0.01"')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"')

    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #chrome_options.binary_location = r'C:\Users\usr\AppData\Local\Google\Chrome\Application'

    chrome_driver = r'C:\chromedriver.exe'
    #driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)

    service = webdriver.chrome.service.Service(chrome_driver)
    service.start()

    urls = ['https://www.asxenergy.com.au/options/au-electricity/HNZ','https://www.asxenergy.com.au/futures_au']

    for i, str_url in enumerate(urls):
        print(f'\n{str_url}')
        driver = webdriver.Remote(service.service_url, desired_capabilities=chrome_options.to_capabilities())
        driver.get(str_url)
        #driver.Navigate().GoToUrl(str_url);

        #driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'u')
        print(driver.page_source)

        #wait = WebDriverWait(driver, 10)
        #elem =driver.find_element_by_css_selector('#my-id')

        xx = driver.execute_script('https://www.asxenergy.com.au/js/options.js?:711')

        #elem = driver.find_element_by_xpath("//body")
        #elem.send_keys(Keys.CONTROL, 'U')

        print('\nxxxxxxxxxxxxxxxxx\n\n\n'+ xx)

        soup = bsoup(driver.page_source,'lxml')
        driver.quit()

        tables = soup.find_all('table')
        table_body = tables[i].find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            vals = [ele.text.strip() for ele in cols]
            print(vals)

```        