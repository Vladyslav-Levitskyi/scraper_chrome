#   This is the second part of code. Run this code after running 'searcher_se.py' and getting
#   'source_file.html'  
import json
from bs4 import BeautifulSoup


content = []

with open("source_file", "r", encoding="utf-8") as file:
    source_file = file.read()
#   Here we have BsScraper class, that has just one classmethod. This method is called general_scraper,
#   and his purpose is to find all needed elements in html skeleton, that we have from 'searcher_se.py'.
class BsScraper:

    def __init__(self, source):
        self.source = source

    @classmethod
    def general_scraper(cls):
        soup = BeautifulSoup(source_file, "html.parser")
        items = soup.find_all("div", class_="shortstory")
        #   Here we need to create <span> list. These spans on purpose website are named equally,
        #   but we must distinguish between them.
        #   And this is the solution: we will use the indexes from list that we will create. Also we
        #   will scrape 'title', 'image_link' and 'product_link' strings with standart BeautifulSoup.
        for item in items:
            span_elements = item.find("div", class_="shortstory__info-wrapper").find_all("span")
            span_list = [span.get_text(strip=True) for span in span_elements]
            content.append({
                "title": item.find("div", class_="shortstory__title").find("a").get_text().strip('\n'),
                "country": span_list[1].split(":", 1)[1].strip(),
                "duration": span_list[3].split(":", 1)[1].strip(),
                "genre": span_list[2].split(":", 1)[1].strip(),
                "year": span_list[0].split(":", 1)[1].strip(),
                "image_link": 'https://kinogo.biz' + str(item.find("div", class_="shortstory__poster").find("img").get("data-src")),
                "product_link": item.find("div", class_="shortstory__poster").find("a").get("href")
            })

        #   Saving product_file.json purpose file.
        with open("product_file.json", "a", encoding="utf-8") as file_json:
            json.dump(content, file_json, indent=4, ensure_ascii=False)
        #   print(*content, sep="\n")


if __name__ == '__main__':
    data_scrape = BsScraper(source_file)
    data_scrape.general_scraper()