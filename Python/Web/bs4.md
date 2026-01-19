# BeautifulSoup

## find href in tag `a` with text `test`
`a class="page-link Pagination__pagelink--3V5Te" href="/property/qld/north-lakes-4509?bedsMin=5&amp;soldHistory=false&amp;rentedHistory=true&amp;types=House&amp;sort=dateSoldNewest&amp;page=1">«</a> `
```py
from bs4 import BeautifulSoup
from selenium import webdriver

# Open Firefox browser and go to website using Selenium
browser = webdriver.Firefox()
browser.get(test_url)

# Get webpage
soup = BeautifulSoup(browser.page_source, 'html.parser')

# Find href of tag with test `test`
tags = soup.find_all('a')
for tag in tags:
    txt = tag.string
    if txt is not None and txt.startswith('test'):
        print(tag['href'])
```

## find href in tag `a` with class `xyz`
`a class="xyz" href="/x/y/z;page=1">1</a>`
```py
tags = soup.find_all('a', class_='xyz')
```

## find div after another div
'''html
<div class="History--xyz">780</div>
<div class="text-secondary">01 Nov 2022</div>
'''

```py
soup = BeautifulSoup(html, 'html.parser')

# Find the value div
value_div = soup.find('div', class_='History--xyz')
value = value_div.text.strip() #780

# Find the next sibling div element after the value_div
date_div = value_div.find_next_sibling('div', class_='text-secondary')
date = date_div.text.strip() #01 Nov 2022
```
