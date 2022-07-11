from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tempfile import mkdtemp
import datetime
import json

JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
date = datetime.datetime.now(JST)

def headless_chrome():
    options = webdriver.ChromeOptions()
    options.binary_location = '/opt/chrome/chrome'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    driver = webdriver.Chrome(
        "/opt/chromedriver",
        options=options
    )
    return driver


def lambda_handler(event, context):

    driver = headless_chrome()

    def get_elm(xpath, sub_xpath):
        global elm
        try:
            elm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        except:
            try:
                elm = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, sub_xpath)))
            except:
                raise
        return elm

    driver.get('https://www.google.com/')

    element = get_elm("//a[text()='Googleについて']", "//*[contains(text(), 'Googleについて')]")

    return {
        'statusCode': 200,
        'date': json.dumps(date, default=str),
        'body': json.dumps(element, default=str),
    }