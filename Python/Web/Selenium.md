# Selenium

https://selenium-python.readthedocs.io/locating-elements.html

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

elems = driver.find_elements_by_xpath('//*[@id]')
for elem in elems:
    print(elem.get_attribute('id'))
```

## Input username/password and submit
```
driver.find_element_by_name("login").send_keys("tutorialspoint")
time.sleep(0.2)
driver.find_element_by_name("passwd").send_keys("pass123")
time.sleep(0.4)
driver.find_element_by_class_name("signinbtn").click()
```
