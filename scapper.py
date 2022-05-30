from configs import Config

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

import time

class Search():

    def __init__(self):
        pass

    def GetDataLinks(self, searchName):
        config = Config()
        driver = config.ChromeSetUp()
        data = []

        try:
            driver.get("https://www.google.com")
            driver.maximize_window()
            time.sleep(10)
            WebDriverWait(driver, 60).until(Ec.presence_of_all_elements_located((By.TAG_NAME, "input")))[0].send_keys(searchName)
            time.sleep(2)
            WebDriverWait(driver, 5).until(Ec.presence_of_all_elements_located((By.TAG_NAME, "input")))[3].click()
            time.sleep(10)
    
            i = 0
            while i < 10:
                nextPages = self.GetData(driver=driver)
                nextBtn = WebDriverWait(driver, 5).until(Ec.presence_of_element_located((By.ID, "pnnext"))).click()
                time.sleep(2)
                i += 1
                data.append(nextPages)
                
        except:
            pass

        return data

    def GetData(self, driver):
        holder = []
        dataHolder = WebDriverWait(driver, 6).until(Ec.presence_of_all_elements_located((By.CLASS_NAME, "g.tF2Cxc")))
        for data in dataHolder:
            links = data.find_elements(By.TAG_NAME, "a")[0].get_attribute("href")
            names = data.find_elements(By.TAG_NAME, "span")[4].get_attribute("innerHTML").split(" ")
            for name in names:
                if "@" in name:
                    email = name.split("@")[0] + "@gmail.com"
                    if len(email.split("@")) == 1:
                        pass
                    else:
                        pair = (f"{links} : {email}")
                        holder.append(pair)
        return holder
        
if __name__ == "__main__":
    serch = Search()
    serch.GetDataLinks('model los angeles "linktr.ee/" @gmail.com site:instagram.com')