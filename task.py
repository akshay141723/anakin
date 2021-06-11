from data_response import response_received
from selenium import webdriver
import time

def search_restaurents_in_manila():
    """
    This function will open  https://food.grab.com/ph/en , search for restaurents in manila
    """
    driver = webdriver.Chrome()
    driver.get("https://food.grab.com/ph/en")
    driver.find_element_by_id('location-input').send_keys('manila')
    driver.find_element_by_id('location-input').click()
    driver.find_element_by_xpath('//button[normalize-space()="Search"]').click()
    data_response = driver.page_source.encode('utf-8')
    time.sleep(20)


def display_latlng():
    """
    This function will print lat and lang of restaurents
    curl 'https://food.grab.com/food-web/v2/search'  --data-raw '{"latlng":"14.520525,121.018479","keyword":"","offset":64,"pageSize":32,"countryCode":"PH"}'
    i have got data from above url, this is the url which returns the restaurents available on the page.
    what you see in response_received is the response which has the data that we are looking for
    """
    merchant_list_on_first_page = response_received['searchResult']['searchMerchants']
    for record in merchant_list_on_first_page:
        restaurent_name = record['address']['name']
        latlng = record['latlng']
        print("=========================================================================================================")
        print ("Restaurant : %s" % (restaurent_name))
        print("Latitude: %s, longitude: %s"% (latlng['latitude'], latlng['longitude']))

if __name__ == '__main__':
    display_latlng()
    search_restaurents_in_manila()