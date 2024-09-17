# Selenium

https://selenium-python.readthedocs.io/locating-elements.html

## check `chromedriver` dependency issue
https://stackoverflow.com/questions/49323099/webdriverexception-message-service-chromedriver-unexpectedly-exited-status-co
```sh
/path/to/chromedriver --version #error while loading shared libraries: libglib-2.0.so.0: cannot open shared object file: No such file or directory
apt-cache search libglib-2.0.so.0
apt-cache madison libglib-2.0.so.0
```

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
## Get form
```
WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.ID, 'username'))
)
form = driver.find_element_by_tag_name('form')
form.find_element_by_id('username').send_keys('usr')
form.find_element_by_id('password').send_keys('pwd')
form.submit()
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
driver.find_element_by_name("login").send_keys("usr")
time.sleep(0.2)
driver.find_element_by_name("passwd").send_keys("pwd")
time.sleep(0.4)
driver.find_element_by_class_name("signinbtn").click()
```
