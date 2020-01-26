from selenium import webdriver
import time


# def totalListings():
#     num_xpath = "//div[contains(@class, 'ais-Panel -stats')]/div[contains(@class, 'ais-Panel-body')]/span"
#     return int(driver.find_element_by_xpath(num_xpath).text.split()[0])

def getListings(search_page):
    # referenced from:
    # https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
    def scrollToBottom():
        SCROLL_PAUSE_TIME = 0.5

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def getListingsElements():
        scrollToBottom()
        return driver.find_elements_by_class_name("feed-item")


    driver = webdriver.Firefox()
    driver.get(search_page)
    if "Page Not Found" in driver.title:
        print("Invalid search url")
        driver.close()
        quit()

    time.sleep(1)
    driver.find_element_by_xpath("//span[text()='Buyer Protection & Authenticity Checks']").click() # summon login popup
    driver.find_element_by_class_name("close").click() # close popup

    listings_elements = getListingsElements()
    listings = []
    for listing_element in listings_elements:
        listings.append(listing_element.find_element_by_tag_name("a").get_attribute("href"))
    return listings

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("search_url")
    URL = parser.parse_args().search_url
    print(getListings(URL))