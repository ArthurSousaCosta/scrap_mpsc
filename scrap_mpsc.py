import pathlib
import os
import shutil
import csv
import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


# Creating empty directory for PDFs (overwrites)
download_dir = str(pathlib.Path(__file__).parent.resolve()) +'\PDFs'
if os.path.exists(download_dir):
    shutil.rmtree(download_dir)
os.makedirs(download_dir)

# Chrome Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
#chrome_options.add_experimental_option('prefs', {
#"download.default_directory": download_dir,
#"download.prompt_for_download": False,
#"download.directory_upgrade": True,
#"plugins.always_open_pdf_externally": True
#})
#chrome_options.use_chromium = True
#chrome_options.add_argument("--headless")
sleep(1)

# Open website
driver = webdriver.Chrome(options=chrome_options)
sleep(1)
action = ActionChains(driver)
driver.get('https://transparencia.mpsc.mp.br/QvAJAXZfc/opendoc.htm?document=portal%20transparencia%5Cportal%20transp%20mpsc.qvw&lang=pt-BR&host=QVS%40qvias&anonymous=true')
sleep(15)

# Click "Atividade-Fim"
driver.find_element(By.XPATH, '//*[@id="8"]/div[2]/table/tbody/tr/td').click()
sleep(15)

# Final list of results
results = []
results_num = 0

# Loop until can't find new document
while True:
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    elements = []

    # Get infos (if it has 'href' gets it (PDF and Movimentação), otherwise gets 'title')
    for e in soup.find_all("div", {"class": "injected"}):
        try:
            elements.append(e.find('a').attrs['href'])
        except:
            elements.append(e.find('div').attrs['title'])

    # Organizing list for csv
    chunk_one = elements[0:int((len(elements)*2/3))]
    chunk_two = elements[int((len(elements)*2/3)):int(len(elements))]
    chunk_one_new = []
    for i in range(0, len(chunk_one), 6):
        chunk_one_new.append(chunk_one[i:i+6])
    chunk_two_new = []
    for i in range(0, len(chunk_two), 3):
        chunk_two_new.append(chunk_two[i:i+3])
    for i in range(len(chunk_two_new)):
        results.append(chunk_one_new[i] + chunk_two_new[i])

    # Remove duplicates, keep order
    results_set = set(tuple(x) for x in results)
    results_list_new = [list(x) for x in results_set]
    results_list_new.sort(key = lambda x: results.index(x))
    results = results_list_new

    # Scrolling down
    if results_num == len(results):
        break
    for i in range(0, 25):
        driver.find_element(By.XPATH, '//*[@id="54"]/div[3]/div[1]/div[4]').click()
    results_num = len(results)

# Close driver
sleep(5)
driver.close()

# Downloading PDFs and indicate its path
for r in range(len(results)):
    link_PDF = results[r][7]
    if 'http' not in link_PDF:
        continue
    num_processo = results[r][0]
    while True:
        try:
            response = requests.get(str(link_PDF))
            new_name = f'{num_processo}.pdf'
            with open(f'{download_dir}\{new_name}', 'wb') as f:
                f.write(response.content)
            results[r][7] = download_dir+'\'+new_name
        except:
            continue
        break

# Creating csv file
with open("result.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(results)