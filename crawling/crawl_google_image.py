from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
import os


pumjong = {
    "예시": ["말라뮤트","시바견"]

}


def crawling(target_name):
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")
    #elem = driver.find_element_by_name("q")
    #elem.send_keys(target_name)
    #elem.send_keys(Keys.RETURN)

    search_box = driver.find_element("name", "q")
    search_box.send_keys(target_name)
    search_box.send_keys(Keys.RETURN)
    #search_box.submit()
    
    # (Seconds) Increase this number if your network is slow
    SCROLL_PAUSE_TIME = 3
    NUMBER_OF_PICTURES = 50  # Increase this number if you want to get more pictures
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    count = 0
    while count < NUMBER_OF_PICTURES:
        # while True:
        # Scroll down to bottom
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                #driver.find_element_by_css_selector(".mye4qd").click()
                driver.find_element(By.CSS_SELECTOR,".mye4qd").click()
            except:
                break
        last_height = new_height

        #images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
        images = driver.find_elements(By.CSS_SELECTOR,".rg_i.Q4LuWd")

        for image in images:
            try:
                image.click()
                time.sleep(2)
                imgUrl = driver.find_element(By.XPATH,
                    '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]').get_attribute("src")
                
                imgUrl = imgUrl.replace('https', 'http')
                opener = urllib.request.build_opener()
                opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
                urllib.request.install_opener(opener)
                
                
                
                urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
                count = count+1
                if count >= (NUMBER_OF_PICTURES+1):
                    break
            except:
                pass


driver = webdriver.Chrome()
for key in pumjong:
    os.makedirs(key, exist_ok=True)
    os.chdir(key)
    for val in pumjong[key]:
        os.makedirs(val, exist_ok=True)
        os.chdir(val)
        crawling(val)
        os.chdir('..')
    os.chdir('..')
driver.close()
