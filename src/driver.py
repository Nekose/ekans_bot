from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
driver = Chrome(options=chrome_options)
driver.get("https://www.google.com")

try:
    google_search = driver.find_element_by_name("q")
    print(f'Found {google_search.tag_name} element with that class name!')
except:
    print("No such luck bucko")

google_search.send_keys("immuno concepts")
google_search.send_keys(Keys.RETURN)


try:
    immuno_concepts = driver.find_element_by_partial_link_text("Immuno Concepts: Home")
    print(f'Found {immuno_concepts.tag_name} element with that class name!')
    immuno_concepts.click()
    WebDriverWait(driver).until()

    print(driver.current_url)
except:
    print("No such luck bucko")



