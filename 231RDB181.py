service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

name=[]
# program reafd information from people.csv file and put all data in name list.
with open("people.csv", "r") as file:
    next(file)
    for line in file:
        row=line.rstrip().split(",") 
        name.append(row)

url = "https://emn178.github.io/online-tools/crc32.html"
driver.get(url)
time.sleep(2)
memoryview
