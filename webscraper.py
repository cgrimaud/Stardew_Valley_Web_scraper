from bs4 import BeautifulSoup
import requests

url_minerals = "https://stardewvalleywiki.com/Minerals"
response = requests.get(url_minerals)
content = BeautifulSoup(response.content, "html.parser")

mineral_table = content.find("table", {"id":"calendartable"})

all_links = mineral_table.findAll('a')

all_minerals = []
for link in all_links:
  all_minerals.append(link.get('title'))

print(content)




