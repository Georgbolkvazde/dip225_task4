import csv
from selenium import webdriver
import time

# Чтение файла people.csv и сохранение данных в списке
people = []
with open('people.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Пропустить заголовок
    for row in reader:
        people.append(row[0])

# Запуск веб-драйвера Selenium
driver = webdriver.Chrome()

# Открытие страницы с tīmekļa rīku
driver.get('https://emn178.github.io/online-tools/crc32.html')

# Итерация по списку людей и получение кодированного значения их полных имен
encoded_names = []
for person in people:
    # Ввод значения в поле ввода
    input_field = driver.find_element_by_id('input')
    input_field.clear()
    input_field.send_keys(person)

    # Нажатие на кнопку "CRC32"
    button = driver.find_element_by_id('crc32_button')
    button.click()

    # Получение кодированного значения
    encoded_name = driver.find_element_by_id('output').text
    encoded_names.append(encoded_name)

    # Пауза для предотвращения блокировки системы безопасности
    time.sleep(1)

# Закрытие веб-драйвера Selenium
driver.quit()

# Чтение файла salary.xlsx и сохранение данных в словаре
salaries = {}
with open('salary.xlsx', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Пропустить заголовок
    for row in reader:
        encoded_name = row[0]
        salary = row[1]
        if encoded_name in salaries:
            salaries[encoded_name].append(salary)
        else:
            salaries[encoded_name] = [salary]

# Ответы на тестовые вопросы
total_salary = {}
for encoded_name, salary_list in salaries.items():
    total_salary[encoded_name] = sum(map(float, salary_list))

# Вывод результатов
for encoded_name, salary in total_salary.items():
    decoded_name = people[encoded_names.index(encoded_name)]
    print(f'Для работника {decoded_name} суммарная зарплата составляет {salary} единиц.')