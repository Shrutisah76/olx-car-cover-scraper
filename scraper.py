from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Configure headless browser
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Target URL
url = "https://www.olx.in/items/q-car-cover"

# Open page
driver.get(url)
time.sleep(5)  # wait for JS to load content

# Fetch item titles and links
items = driver.find_elements(By.CSS_SELECTOR, "li.EIR5N")  # OLX item cards
results = []

for item in items:
    try:
        title_elem = item.find_element(By.CSS_SELECTOR, "span._2tW1I")
        link_elem = item.find_element(By.TAG_NAME, "a")
        title = title_elem.text.strip()
        link = link_elem.get_attribute("href")
        results.append(f"{title}\n{link}\n")
    except Exception as e:
        continue

# Save to file
with open("olx_car_covers.txt", "w", encoding="utf-8") as f:
    f.writelines("\n".join(results))

# Close browser
driver.quit()

print("Scraped results saved to 'olx_car_covers.txt'")
