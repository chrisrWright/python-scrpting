from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from names import form_data

# set up the driver
driver = webdriver.Chrome(r'C:\Users\chris\Documents\drivers\chromedriver.exe')

# navigate to the form
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSd9Kzwm25rRKIvQSig3pzX_rEi7nIYMRJAqUf6dT6_s4QqlNw/viewform")

# wait for the form to load
time.sleep(5)

# Find the form fields by name or ID and fill them in with the corresponding data from the array
for data in form_data:
    name_field = driver.find_element(By.XPATH ,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    email_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name_field.send_keys(data[0])
    email_field.send_keys(data[1])
    checkbox_field = driver.find_element(By.ID, 'i14')
    checkbox_field.click()
   # time.sleep(15)
    # Submit the form
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()

    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSd9Kzwm25rRKIvQSig3pzX_rEi7nIYMRJAqUf6dT6_s4QqlNw/viewform")
  
    time.sleep(1)

time.sleep(1)

# close the driver
driver.close()
