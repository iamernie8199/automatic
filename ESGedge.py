import os

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from joblib import Parallel, delayed


if not os.path.exists('ESG'):
    os.makedirs('ESG')
pic_savepath = os.path.join(os.getcwd(), 'ESG')

options = Options()
prefs = {
    'savefile.default_directory': pic_savepath
}
options.add_experimental_option('prefs', prefs)
options.add_argument('--kiosk-printing')

def take_screenshot(company):
    company += ' ESG 環境保護 社會責任 公司治理'
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options = options)
    driver.get(f"https://www.google.com/search?q={company}&tbm=nws")
    # driver.execute_script('window.print();')
    driver.get_screenshot_as_file(f'{pic_savepath}/{company}.png')
    driver.close()

with open('名稱.txt', 'rt', encoding='utf-8') as f:
    company_name = f.read().replace('\n', '')
company_name = company_name.split('^')
Parallel(n_jobs=2)(delayed(take_screenshot)(c) for c in company_name)
