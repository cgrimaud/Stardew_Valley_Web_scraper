from bs4 import BeautifulSoup
import requests

url_minerals = "https://stardewvalleywiki.com/Minerals"
response = requests.get(url_minerals)
content = BeautifulSoup(response.content, "html.parser")

# mineral_table = content.find("table", {"id":"calendartable"})
# all_links = mineral_table.findAll('a')
# all_minerals = []
# for link in all_links:
#   all_minerals.append(link.get('title'))
# print(all_minerals)

content_div = content.find('div', {'class': 'mw-content-ltr'})
content_tables = content_div.find_all('td')
tables = []
for table in content_tables:
    tables.append(table.text)
#content_body_contents = content_table_body.find_all('td')

print (tables)

#print(all_tables)
