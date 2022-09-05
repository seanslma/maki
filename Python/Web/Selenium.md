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
