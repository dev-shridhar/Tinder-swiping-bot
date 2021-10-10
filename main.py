from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep

EMAIL = "sidkulkarnimj@gmail.com"

PASSWORD = "9881823532"

chrome_driver_path = "F:/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://www.tinder.com")

log_in = driver.find_element_by_xpath('//*[@id="q-1826079426"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in.click()

sleep(2)

try:
    login_facebook = driver.find_element_by_xpath('//*[@id="q-1604738990"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    login_facebook.click()
except:
    try:
        more_options = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/button')
        more_options.click()
    except StaleElementReferenceException:
        login_facebook = driver.find_element_by_xpath('//*[@id="q-1604738990"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        login_facebook.click()

finally:
    login_facebook = driver.find_element_by_xpath('//*[@id="q-1604738990"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    login_facebook.click()


sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')
email.send_keys(EMAIL)
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)

sleep(5)

allow_location = driver.find_element_by_xpath('//*[@id="q-1604738990"]/div/div/div/div/div[3]/button[1]')
allow_location.click()

enable_notification = driver.find_element_by_xpath('//*[@id="q-1604738990"]/div/div/div/div/div[3]/button[1]')
enable_notification.click()
# try:
#     allow_messsages = driver.find_element_by_xpath('//*[@id="q-1604738990"]/div/div/div/div/div[3]/button[1]')
#     allow_messsages.click()

for n in range(100):

    sleep(1)
    try:
        like_button = driver.find_element_by_xpath('//*[@id="q-1826079426"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
        like_button.click()
    except:
        match_popup = driver.find_element_by_css_selector(".itsAMatch a")
        match_popup.cl

        sleep(2)

driver.quit()
