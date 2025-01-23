# Selenium
- https://pypi.org/project/selenium/
- https://selenium-python.readthedocs.io/locating-elements.html

## how to install
discussions:
- https://github.com/password123456/setup-selenium-with-chrome-driver-on-ubuntu_debian
- https://stackoverflow.com/questions/22476112/using-chromedriver-with-selenium-python-ubuntu

chromium browser download
- https://packages.debian.org/sid/amd64/chromium/download

chromium and chromedriver download (right place to download packages for 18.04)
- http://ftp.ubuntu.com/ubuntu/ubuntu/pool/universe/c/chromium-browser/
- chromium-browser_112.0.5615.49-0ubuntu0.18.04.1_amd64.deb
- chromium-chromedriver_112.0.5615.49-0ubuntu0.18.04.1_amd64.deb

install them in dockerfile
```dockerfile
USER root

# install version-pinned chromium-browser and chromedriver
RUN apt-get update && \
    apt-get install -y libnss3 libnssutil3 libnspr4 && \
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

## disable `Error sending stats to Plausible`
```
WARNING
selenium.webdriver.common.selenium_manager
Error sending stats to Plausible: error sending request for url (https://plausible.io/api/event)
```

Solution: 
- disable Selenium from sending anonymous usage statistics
- https://www.selenium.dev/documentation/selenium_manager/#data-collection
- set the `SE_AVOID_STATS` environment variable to `true`, or
-  set `avoid-stats = true` in config file

## WebDriverException: Message: Service chromedriver unexpectedly exited. Status code was: 127
https://stackoverflow.com/questions/49323099/webdriverexception-message-service-chromedriver-unexpectedly-exited-status-co
- Reason: some dependencies are missing. 
- Solution: check and install missing depencdencies

## check `chromedriver` dependency issue
https://stackoverflow.com/questions/49323099/webdriverexception-message-service-chromedriver-unexpectedly-exited-status-co
```sh
user@xyz:~$ /path/to/chromedriver --version
/path/to/chromedriver: error while loading shared libraries: libnss3.so: cannot open shared object file: No such file or directory
#will show all depedencies
user@xyz:~$ ldd /path/to/chromedriver
        linux-vdso.so.1 (0x00007ffdd63e1000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fe8b09af000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fe8b09aa000)
        libglib-2.0.so.0 => /lib/x86_64-linux-gnu/libglib-2.0.so.0 (0x00007fe8b0870000)
        libnss3.so => not found
        libnssutil3.so => not found
        libnspr4.so => not found
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fe8b0787000)
        libxcb.so.1 => /lib/x86_64-linux-gnu/libxcb.so.1 (0x00007fe8b075d000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007fe8b073d000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fe8b0514000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fe8b1a88000)
        libpcre.so.3 => /lib/x86_64-linux-gnu/libpcre.so.3 (0x00007fe8b049e000)
        libXau.so.6 => /lib/x86_64-linux-gnu/libXau.so.6 (0x00007fe8b0496000)
        libXdmcp.so.6 => /lib/x86_64-linux-gnu/libXdmcp.so.6 (0x00007fe8b048e000)
        libbsd.so.0 => /lib/x86_64-linux-gnu/libbsd.so.0 (0x00007fe8b0476000)
        libmd.so.0 => /lib/x86_64-linux-gnu/libmd.so.0 (0x00007fe8b0469000)
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

## ubuntu 22.04
how-to-install-chromium-without-snap: https://askubuntu.com/questions/1204571/how-to-install-chromium-without-snap
- For 22.04, use the package from Debian bullseye instead of buster
- see metrizable's answer: https://github.com/googlecolab/colabtools/issues/3347
