from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


def main():
    views = int(input("Enter the amount of views requested: "))
    for i in range(views):
        options = webdriver.FirefoxOptions()
        options.set_preference("media.volume_scale", "0.0")
        options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
        p_link = "https://www.croxyproxy.com/"
        t_link = ""  # This field is where the user must paste the link to the Twitch channel they wish to create artificial viewers for
        driver.get(p_link)
        driver.implicitly_wait(5)
        gotoChannel(driver, t_link)
        driver.implicitly_wait(10)


def gotoChannel(driver, link):
    search_ref = '//*[@id="url"]'
    button_ref = '//*[@id="requestSubmit"]'
    search_field = driver.find_element(by=By.XPATH, value=search_ref)
    search_button = driver.find_element(by=By.XPATH, value=button_ref)
    ActionChains(driver) \
        .scroll_by_amount(300, 300) \
        .pause(1) \
        .click(search_field) \
        .pause(1) \
        .send_keys_to_element(search_field, link) \
        .pause(1) \
        .click(search_button) \
        .pause(45) \
        .perform()


main()
