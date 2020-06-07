from bs4 import BeautifulSoup
import requests

class Bundle:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_items(self):
        content = " "
        for item in self.items:
            content += item 
        return content


    def __str__(self):
        return "{}: \n{}".format(self.name, self.get_items())




url_bundles = "https://stardewvalleywiki.com/Bundles"
response = requests.get(url_bundles)
content = BeautifulSoup(response.content, "lxml")
#print(content.prettify())
tables = content.find_all('table', {"class":"wikitable", "style": None})

bundles = []
for table in tables[0:26]:
    header = table.find('th')
    bundle_name = header.text[:-1]
    rows = table.find_all('td')  
    bundle_items = [] 
    for row in rows[2:-2:2]:
        item_name = row.text.lstrip()
        bundle_items.append(item_name)
    bundle_object = Bundle(bundle_name, bundle_items)
    bundles.append(bundle_object)

for bundle in bundles:
    print(bundle)

########### Create Dictionary of Bundle Names: Bundle Items #########
# bundle_names = []
# bundle_items = []
# for table in tables[0:26]:
#     header = table.find('th')
#     bundle_names.append(header.text[:-1])
#     rows = table.find_all('td')
#     items = []
#     for row in rows[2:-2:2]:
#         item_name = row.text.lstrip()
#         items.append(item_name[:-1])
#     bundle_items.append(items)

# bundle_dictionary = dict(zip(bundle_names, bundle_items))

    




    