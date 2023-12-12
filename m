import csv
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

# Reading data from people.csv
people = []
with open('people.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    for row in reader:
        people.append(row[0])  # Assuming the name is in the first column

# Setting up the Selenium web driver
service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

# URL of the web tool
url = "https://emn178.github.io/online-tools/crc32.html"
driver.get(url)
time.sleep(2)  # Allow time for the page to load

# List to store encoded names
encoded_names = []

# Iterating through names and getting CRC32 encoding
for person in people:
    input_field = driver.find_element_by_id('input')
    input_field.clear()
    input_field.send_keys(person)

    # Clicking the "CRC32" button
    button = driver.find_element_by_id('crc32_button')
    button.click()

    # Getting the encoded value
    encoded_name = driver.find_element_by_id('output').text
    encoded_names.append(encoded_name)

    # Pause to prevent system lock
    time.sleep(1)

# Closing the web driver
driver.quit()

# Now you have the encoded names in the 'encoded_names' list.
# You can proceed with further processing, e.g., reading and analyzing 'salary.xlsx'.

# If you have specific questions or issues with a part of your code, feel free to share that part for more targeted help.
