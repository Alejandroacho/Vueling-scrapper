from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--no-sandbox')
driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=DesiredCapabilities.CHROME,
    options=options
)

URL = "https://www.rd.com/jokes/"
driver.get(url=URL)
print(driver.page_source)