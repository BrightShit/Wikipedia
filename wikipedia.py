
from selenium import webdriver
import time
import os
def planets():

    planet=input("Choose the planet that you would like to get information about: \n")

    PATH='chromedriver.exe'
    
    driver = webdriver.Chrome(PATH)

    source=driver.get('https://en.wikipedia.org/wiki/'+planet)

    test=driver.find_element_by_xpath(xpath="//*[@id=\"mw-content-text\"]/div[1]/p[3]")

    file = open ('info.txt','w+')
    file.write(test.text)
    file.close()

    os.startfile('info.txt')
    
    time.sleep(1000)

planets()
