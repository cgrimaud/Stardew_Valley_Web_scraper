from bs4 import BeautifulSoup
import requests
from sdv_classes import Bundle, CommunityCenterRoom
# needed for OrderedDict
from collections import OrderedDict
# needed to clear screen
import os


def scrape_web_page():
    url_bundles = "https://stardewvalleywiki.com/Bundles"
    response = requests.get(url_bundles)
    content = BeautifulSoup(response.content, "lxml")
    return content

def get_all_rooms():
    """ Returns complete list of CommunityCenterRoom objects """
    data = scrape_web_page()
    return parse_rooms(data) 

def parse_rooms(data):
    """ returns a list of CommunityCenterRoom Objects
    Parameters: 
        data: passed from get_all_rooms, which is the website data parsed by bs
    Returns:
        rooms list: A complete list of CommunityCenterRoom Objects
    """
    room_names = data.find_all('h2')
    rooms = []
    for r_name in room_names[2:8]:       
        room_bundles = parse_room_bundles(data, r_name.text)
        rooms.append(CommunityCenterRoom(r_name.text, room_bundles))
    return rooms    

def parse_room_bundles(data, room_name):
    """ Parses beautifulsoup object to create a Bundle object if bundle is associated with room_name pased in  
    Parameters: 
        data: passed from parse_rooms(), website data parsed by bs
        room_name: passed from parse_room() for loop. 
    Returns:
        List of Bundle Objects associated with a specific community center room
    """
    bundles = []
    tables = data.find_all('table', {"class":"wikitable", "style": None})  
    for table in tables[0:30]:
        # Gets coummunity center room name associated with the bundle
        cc_room = table.find_previous_sibling('h2').text
        if room_name == cc_room:
            # Gets bundle name
            bundle_name = table.find('th').text[1:-1]
            # Gets items inside of bundle
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
        
            # Gets number of required items to complete bundle
            required_items = 0    
            for row in rows[1].find_all(recursive=False):
                if row:
                    required_items += 1
        
            # create Bundle objects and append objects to a list
            bundle_object = Bundle(bundle_name, bundle_items, required_items, cc_room)
            bundles.append(bundle_object)

    return bundles



##### Menu Features ### 
def clear():
    os.system('cls' if os.name =='nt' else 'clear')

def view_rooms():
    """ View List of Community Center Rooms """
    # rooms = get_all_rooms()
    # choice = None

    # print("#"*20)
    # for room in rooms:
    #     print('{}) {}'.format(room.get_room_id(), room.get_name()))
    # print("#"*20)
    # print("Enter room number you would like to view\n(Enter 'q' to quit)")
    # choice = input('Selection: ').lower().strip()
    # if choice == 'q':
    #     break
    # else:
    pass
        
def view_bundles():
    """ View list of Bundles """
    pass

def view_items():
    """ View bundle items """

def menu_loop():
    """ Show the main menu """
    choice = None
    print("Welcome to the Stardew Valley Community Center Bundle Tracker!")
    while choice != 'q':    
        print("Enter 'q' to quit.")
        for key, value in main_menu.items():
              print('{}) {}'.format(key, value.__doc__))
        choice = input('Selection: ').lower().strip()
        
        if choice in main_menu:
            clear()
            main_menu[choice]()


main_menu = OrderedDict([
    ('1', view_rooms),
    ('2', view_bundles),
])

room_menu = OrderedDict([
    ('1', view_bundles),
    ('2', view_items)
])

menu_loop()