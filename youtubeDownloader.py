from selenium import webdriver
import time
driver = webdriver.Firefox()
url = r"https://www.youtube.com/playlist?list=PLGFbCf41_6ZatogvB998maCt2PYy1UYyh"   #url of youtube playlist
driver.get(url)
total_videos = len(driver.find_elements_by_id('video-title'))
print("Total Videos are ",total_videos)
for i in range(total_videos):
    driver.get(url)
    driver.find_elements_by_id('video-title')[i].click()
    string = driver.current_url
    string = string[:12]+'ss'+string[12:]
    driver.get(string)
    time.sleep(10)
    driver.find_elements_by_xpath(r"/html/body/div/div[1]/div[3]/div[4]/div/div[1]/div[2]/div[2]/div[1]/a")[0].click()
driver.close()
