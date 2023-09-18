from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

# Initialize the webdriver
driver = webdriver.Chrome() #path to your Chrome WebDriver.exe

# Navigate to the BBC News website
url = 'https://www.bbc.com/news'
driver.get(url)

# Find and extract the headlines
headlines = driver.find_elements(By.CLASS_NAME, 'gs-c-promo-heading')

# Create a CSV file and write the headlines
with open('bbc_headlines.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Headline']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for headline in headlines:
        title = headline.text.replace('\n', ' ')
        writer.writerow({'Headline': title})

# Clean up and close the webdriver
driver.quit()


 