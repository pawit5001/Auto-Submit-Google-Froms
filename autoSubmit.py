from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# Google Forms Link
form_url = "https://docs.google.com/forms/d/e/xxxx/viewform"

def select_option(answer):
    try:
        option = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, answer))
        )
        option.click()
        time.sleep(0.5)
    except Exception as e:
        print(f"No choices found: {answer} | Error: {e}")

# Loop 10 rounds
for i in range(10):
    print(f"Doing round {i+1}...".encode("utf-8", errors="ignore").decode("utf-8"))

    driver.get(form_url)
    time.sleep(3)  
    
    if i < 39: 
        q1_answer = "//*[@id='xxxx']/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[2]/div/span" # select choice 1 = 39 times
    else:
         q1_answer = "//*[@id='xxxx']/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[2]/div/span" # select choice 2 = 61 times
    select_option(q1_answer)
    
    # Submit
    try:
        submit_button = driver.find_element(By.XPATH, "//*[@id='xxxx']/div[2]/div/div[3]/div[1]/div[1]/div/span")
        submit_button.click()
        time.sleep(2)
    except Exception as e:
        print(f"Can't submit | Error: {e}")

    print(f"Round {i+1} submitted successfully!")

print("All Done!")
driver.quit()
