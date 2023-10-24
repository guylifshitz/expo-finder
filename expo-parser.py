from bs4 import BeautifulSoup
import pandas as pd
import os

events_dict_list = []

def get_special_locations():
    locations = pd.read_csv("configure/locations.csv", encoding='utf8').drop_duplicates()
    return locations["Location"].sort_values().values

special_locations = get_special_locations()

for i in range(1, 25):
    with open(f"downloads/{i}.html", "r") as f:
        contents = f.read()

        soup = BeautifulSoup(contents, "html.parser")

        events = soup.find_all(class_="event-name-rating")
        for event in events:
            title = event.find(class_="event-title").get_text().strip()

            link = event.find("a", {"itemprop": "url"})["href"]
            start_date = event.find("meta", {"itemprop": "startDate"})["content"]
            end_date = event.find("meta", {"itemprop": "endDate"})["content"]

            location = event.find(class_="metalocation")
            location = location.find("meta", {"itemprop": "name"})["content"]

            special_location = location in special_locations
            
            print()
            print(title)
            print(location)
            print(link)
            print(start_date)
            print(end_date)

            events_dict_list.append(
                {
                    "title": title,
                    "location": location,
                    "special_location": special_location,
                    "link": link,
                    "start_date": start_date,
                    "end_date": end_date,
                }
            )

df = pd.DataFrame(events_dict_list).drop_duplicates()

outdir = 'output'
if not os.path.exists(outdir):
    os.mkdir(outdir)
df.to_csv("output/output-events.csv")
