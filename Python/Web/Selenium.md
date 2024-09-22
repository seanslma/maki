# Selenium

https://selenium-python.readthedocs.io/locating-elements.html

## how to install
discussions:
- https://github.com/password123456/setup-selenium-with-chrome-driver-on-ubuntu_debian
- https://stackoverflow.com/questions/22476112/using-chromedriver-with-selenium-python-ubuntu

chronium browser download
- https://packages.debian.org/sid/amd64/chromium/download

chronium and chromedriver download (right place to download packages for 18.04)
- http://ftp.ubuntu.com/ubuntu/ubuntu/pool/universe/c/chromium-browser/
- chromium-browser_112.0.5615.49-0ubuntu0.18.04.1_amd64.deb
- chromium-chromedriver_112.0.5615.49-0ubuntu0.18.04.1_amd64.deb

install them in dockerfile
```dockerfile
USER root

# install version-pinned chromium-browser and chromedriver
RUN apt-get update && \
    url="http://ftp.ubuntu.com/ubuntu/ubuntu/pool/universe/c/chromium-browser/" && \
    curl -L -o chromium-browser.deb ${url}chromium-browser_112.0.5615.49-0ubuntu0.18.04.1_amd64.deb && \
    apt-get -f install -y ./chromium-browser.deb && \
    rm -rf chromium-browser.deb && \
    curl -L -o chromium-chromedriver.deb ${url}chromium-chromedriver_112.0.5615.49-0ubuntu0.18.04.1_amd64.deb && \
    apt-get -f install -y ./chromium-chromedriver.deb && \
    rm -rf chromium-chromedriver.deb

USER user

# Add to path var
ENV CHROMEDRIVER_PATH="/usr/lib/chromium-browser/chromedriver" \
    PATH="${CHROMEDRIVER_PATH}:${PATH}"
```

## use it in python
```py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Setup Chrome driver
# executable_path = os.environ.get('CHROMEDRIVER_PATH')
# service = Service(executable_path=executable_path)
service = Service() # executable_path is not required, added to path var
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')  # Avoid sandbox issues
chrome_options.add_argument('--headless')    # Run in headless mode
chrome_options.add_argument('--disable-dev-shm-usage')  # Avoid resource limits
driver = webdriver.Chrome(service=service, options=chrome_options)

# get web content
driver.get(url)
WebDriverWait(driver, timeout).until(
    expected_conditions.presence_of_element_located((By.ID, 'password'))
)
driver.find_element('id', 'username').send_keys(config['username'])
driver.find_element('id', 'password').send_keys(config['password'])
driver.find_element('id', 'submit_row').submit()
```

## check `chromedriver` dependency issue
https://stackoverflow.com/questions/49323099/webdriverexception-message-service-chromedriver-unexpectedly-exited-status-co
```sh
/path/to/chromedriver --version #error while loading shared libraries: libglib-2.0.so.0: cannot open shared object file: No such file or directory
ldd /path/to/chromedriver       #will show all depedencies
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
