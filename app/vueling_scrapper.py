import email.message
import getpass
import os
import smtplib
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager

DEPLOYED = True
LAST_SLIDES = 0
VUELING_URL = "https://www.vueling.com/es"

class VuelingScrapper:

    def __init__(self):
        self.main()

    def main(self):
        server, sender = self.get_email_sender_and_server()
        emails = self.get_emails()
        driver = self.get_chrome_driver()
        self.allow_cookies(driver)
        self.look_for_slides_changes(sender, emails, server, driver)

    def get_email_sender_and_server(self):
        while True:
            try:
                sender = input("Email sender: ")
                password = getpass.getpass()
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender, password)
                break
            except:
                print("Error getting email sender and server")
                print("Please try again")
        return server, sender

    def get_emails(self):
        while True:
            try:
                number_of_emails = int(input("Number of emails: "))
                break
            except:
                print("Please insert a valid number")
        emails = []
        for number in range(number_of_emails):
            email = input(f"Email {number + 1}: ")
            emails.append(email)
        return emails

    def get_chrome_driver(self):
        # Service method (current one)
        # service = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=service)
        
        # Driver method (deprecated)
        # driver = webdriver.Chrome('path')

        # Remote method
        options = self.get_chrome_options()
        driver = webdriver.Remote('http://selenium:4444/wd/hub', 
                                  options=options)

        driver.get(VUELING_URL)
        return driver

    def get_chrome_options(self):
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument('--disable-dev-shm-usage')
        return chrome_options

    def allow_cookies(self, driver):
        wait = WebDriverWait(driver, 15)
        element = wait.until(expected_conditions.presence_of_all_elements_located((By.ID, 'ensCloseBanner')))
        element[0].click()
    
    def look_for_slides_changes(self, sender, emails, server, driver):
        global LAST_SLIDES
        while True:
            slider = driver.find_element(By.ID, "slideshowContaineBanner")
            slider_count = slider.get_attribute("childElementCount")
            if slider_count != LAST_SLIDES:
                for email in emails:
                    try:
                        message = self.make_message(sender, email)
                        server.sendmail(sender, email, message)
                    except:
                        print("Error sending email")
            LAST_SLIDES = int(slider_count)
            time.sleep(7200)

    def make_message(self, sender, receiver_email):
        message = email.message.Message()
        message['From'] = str(sender)
        message['To'] = str(receiver_email)
        message['Subject'] = "Vueling slider has changed!"
        message.set_payload("Maybe there is a slide with an offer! :D")
        return message.as_string()

VuelingScrapper()