import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

BASE_URL = "http://quotes.toscrape.com"
driver.get(BASE_URL)

quotes = []
authors_seen = set()
authors_data = []


def scrape_author_info(link):
    sleep(1)
    name = driver.find_element(By.TAG_NAME, "h3").text
    birth_date = driver.find_element(By.CLASS_NAME, "author-born-date").text
    birth_place = driver.find_element(By.CLASS_NAME, "author-born-location").text
    description = driver.find_element(By.CLASS_NAME, "author-description").text.strip()
    return {
        "name": name,
        "birth_date": birth_date,
        "birth_place": birth_place,
        "description": description,
    }

while True:
    sleep(1)
    quote_elements = driver.find_elements(By.CLASS_NAME, "quote")

    for container in quote_elements:
        try:
            text = container.find_element(By.CLASS_NAME, "text").text
            author = container.find_element(By.CLASS_NAME, "author").text
            tags = [tag.text for tag in container.find_elements(By.CLASS_NAME, "tag")]

            quotes.append({"quote": text, "author": author, "tags": tags})

            if author not in authors_seen:
                authors_seen.add(author)
                author_link = container.find_element(By.TAG_NAME, "a").get_attribute(
                    "href"
                )

                # відкриваємо нову вкладку
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[1])
                driver.get(author_link)
                sleep(1)

                author_info = scrape_author_info(author_link)

                authors_data.append(author_info)

                driver.close()
                driver.switch_to.window(driver.window_handles[0])

        except Exception as e:
            print("Error while scraping quote:", e)

    # переходимо на наступну сторінку
    try:
        next_button = driver.find_element(By.CLASS_NAME, "next")
        next_link = next_button.find_element(By.TAG_NAME, "a").get_attribute("href")
        driver.get(next_link)
    except:
        print("No more pages to scrape.")
        break


# Зберігаємо в JSON файли
with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(quotes, f, indent=2, ensure_ascii=False)

with open("authors.json", "w", encoding="utf-8") as f:
    json.dump(authors_data, f, indent=2, ensure_ascii=False)

driver.quit()
