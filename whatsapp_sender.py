from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chat_name = raw_input("Enter chat-name")
chat_message = raw_input("Enter message")

driver = webdriver.Firefox()
driver.maximize_window()

try:

    driver.get("https://web.whatsapp.com")

    print "Waiting for QR code to be scanned"

    time.sleep(20)

    search_path = "//input[@class='input input-search']"

    search_box = driver.find_element_by_xpath(search_path)

    search_box.send_keys(chat_name)

    time.sleep(5)

    print "Searching for desired chat"

    path = "//div[@class='chat-title']/span[.='" + chat_name + "']"

    elem = driver.find_element_by_xpath(path)
    elem.click()

    print "Chat selected"
    print "Sending message in a while"

    time.sleep(20)

    input_path = "//div[@class='input']"
    text_field = driver.find_element_by_xpath(input_path)

    i = 0
    while i < 500:
        text_field.send_keys(chat_message)
        text_field.send_keys(Keys.ENTER)
        i += 1

    print "Completed"

except:

    print "Error occurred"
    driver.quit()
