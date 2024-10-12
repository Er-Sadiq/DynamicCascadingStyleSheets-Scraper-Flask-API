from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def scraperFn(query):
    
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")  # Run headless if you don't need a GUI
    with webdriver.Firefox(options=options) as driver:
        driver.get(query)

        # Wait for the page to load
        try:
            
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "body")) 
            )
        except TimeoutException:
            print("Error: Timeout waiting for page to load.")
            return {"error": "Timeout waiting for page to load."}

        # Get the full page HTML content
        html_content = driver.page_source

        return html_content  
