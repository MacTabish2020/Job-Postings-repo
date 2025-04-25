from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  # no options needed
driver.set_window_size(1920, 1080)

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

driver.execute_cdp_cmd("Network.setUserAgentOverride", {
    "userAgent": user_agent
})

for page in range(1, 101):
    url = f"https://www.naukri.com/it-jobs-{page}?src=gnbjobs_homepage_srch"
    driver.get(url)

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "title"))
    )

    html = driver.page_source

    with open(f'naukri_page_{page}.html', 'w', encoding='utf-8') as f:
        f.write(html)

driver.quit()