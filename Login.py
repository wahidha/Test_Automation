import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class ListInvestasi(unittest.TestCase):

    #steps
        driver= webdriver.Chrome() #buka web browser
        driver.get("https://shafiq.id/login") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("wahid@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("Wahid1222") # isi password
        time.sleep(1)
    

    #Elemen checkbox reCAPTCHA
        checkbox = driver.find_element(By.CLASS_NAME,"g-recaptcha")

    #Klik kotak centang
        checkbox.click()
        time.sleep(2)

    #Klik Masuk
        driver.find_element(By.ID, "Masuk").click()
        time.sleep(1)

        driver.quit()
if __name__ == "__main__":
    unittest.main()