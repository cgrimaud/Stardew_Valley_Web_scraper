from bs4 import BeautifulSoup
import requests

class Bundle:
    def __init__(self, name, items, amt_to_complete):
        self.name = name
        self.items = items
        self.amt_to_complete = amt_to_complete

    def get_items(self):
        content = "\n"
        for item in self.items:
            content += item
        return content


    def __str__(self):
        return "***{}({})***{}".format(self.name, self.amt_to_complete, self.get_items())




url_bundles = "https://stardewvalleywiki.com/Bundles"
response = requests.get(url_bundles)
content = BeautifulSoup(response.content, "lxml")
tables = content.find_all('table', {"class":"wikitable", "style": None})

bundles = []
for table in tables[0:26]:
    header = table.find('th')
    bundle_name = header.text[1:-1]
    if "Quality" not in bundle_name:
        rows = table.find_all('td')  
        bundle_items = [] 
        for row in rows[2:-2:2]:
            item_name = row.text.lstrip()
            bundle_items.append(item_name)
    else:
        rows = table.find_all('td')
        bundle_items = []
        for row in rows:
            tbl_row = row.find_all('table')
            for tbl in tbl_row:
                bundle_items.append(tbl.text.lstrip() + '\n')

    ## Get number of required items to complete bundle
    required_items = 0    
    for row in rows[1].find_all(recursive=False):
        if row:
            required_items += 1

    # create Bundle objects and append object to a list
    bundle_object = Bundle(bundle_name, bundle_items, required_items)
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

    




    