# Selenium

## Screenshot: available via screen
```
driver = webdriver.PhantomJS()
driver.set_window_size(1920,1080)
try:
    driver.get('http://example.com/')
except Exception as exc:
    driver.save_screenshot('screenshot.png')
driver.close()
```

## List all elments Ids - slow but works
```
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://example.com')

ids = driver.find_elements_by_xpath('//*[@id]')
for id in ids:
    print id.get_attribute('id')
```
