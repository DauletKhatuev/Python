from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Путь к geckodriver 
service = Service("C:/tools/geckodriver.exe")

# Запуск Firefox
driver = webdriver.Firefox(service=service)

try:
    # 1. Открыть сайт
    driver.get("https://itcareerhub.de/ru")

    # 2. Переход в раздел «Способы оплаты»
    # Ищем ссылку по тексту
    payment_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Способы оплаты"))
    )
    payment_link.click()

    print("Раздел 'Способы оплаты' успешно открыт!")

finally:
    import time
    time.sleep(5)
    driver.quit()
