import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Daftar(unittest.TestCase):

    #steps
        driver= webdriver.Chrome() #buka web browser
        driver.get("https://www.shafiq.id/signup/form/personal") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"name").send_keys("wahid habibullah") # isi nama
        time.sleep(1)
        driver.find_element(By.ID,"email").send_keys("wahid@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("Wahid12345678") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"confirm_password").send_keys("Wahid12345678") # isi password
        time.sleep(1)

    #Elemen checkbox reCAPTCHA
        checkbox = driver.find_element(By.CLASS_NAME,"g-recaptcha")

    #Klik kotak centang
        checkbox.click()
        time.sleep(4)

    #Klik Daftar
        driver.find_element(By.ID, "Daftar").click()
        time.sleep(1)

if __name__ == "__main__":
    unittest.main()