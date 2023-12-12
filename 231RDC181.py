import pandas as pd
from selenium import webdriver
import time
import zlib

# Funkcija, lai iegūtu kodēto vārdu izmantojot CRC32
def get_encoded_name(name):
    driver = webdriver.Chrome()  # Jāielādē chromedriver vai citu pārlūka draiveri
    driver.get("https://emn178.github.io/online-tools/crc32.html")

    # Ievada vārdu tīmekļa rīkā un sagaida, kamēr iegūs rezultātu
    input_element = driver.find_element_by_id("inputText")
    input_element.clear()
    input_element.send_keys(name)
    time.sleep(1)  # Pauze, lai rīks izpilda kodēšanu
    result_element = driver.find_element_by_id("result")
    encoded_name = result_element.get_attribute("value")

    driver.quit()  # Aizvēr pārlūka logu
    return encoded_name

# Ielādē people.csv datni un nolasa darbinieku vārdus
people_df = pd.read_csv("people.csv")
encoded_names = []

# Iegūst katram darbiniekam kodēto vārdu un saglabā to sarakstā
for index, row in people_df.iterrows():
    full_name = f"{row['Vārds']} {row['Uzvārds']}"
    encoded_name = get_encoded_name(full_name)
    encoded_names.append(encoded_name)

# Pievieno kodētos vārdus people.csv datnes kolonnā
people_df['EncodedName'] = encoded_names

# Ielādē salary.xlsx datni
salary_df = pd.read_excel("salary.xlsx")

# Apvieno abas datnes pēc kodētā vārda
merged_df = pd.merge(people_df, salary_df, left_on='EncodedName', right_on='A')

# Izvada rezultātu
print(merged_df[['Vārds', 'Uzvārds', 'Alga']])