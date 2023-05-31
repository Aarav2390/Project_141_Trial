from bs4 import BeautifulSoup
import requests

# url of website
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

#headers array
headers = ["name","distance","mass","radius"]

#array to store star data
star_data = []

response = requests.get(START_URL, verify=False)

def scrape():
    for i in range(0,1):
        print(f'Scraping Page {i+1}')
        soup = BeautifulSoup(response.get_source,"html.parser")

        for tr_tags in soup.find_all("tr"):
            td_tags = tr_tags.find_all("td")
            temp_list = []

            for index, td_tag in enumerate(td_tags):
                if index == 1:
                    temp_list.append(td_tag.find_all("a")[1].contents[0])
                elif index == 3:
                    temp_list.append()