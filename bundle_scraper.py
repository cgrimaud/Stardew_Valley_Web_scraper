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
    content = BeautifulSoup(response.content, "html.parser")
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

def show_menu(choices, allow_cancellation=False):
    """
    Display a command-line menu to the user, and let them make a selection

        :param choices: A list of the options to display in the menu
        :param allow_cancellation: If the user should be able to exit the menu without making a selection (default False)
        :returns: The selection of the user, or None if cancelled.
    """
    options = {}
    # Print the options out to the user, enumerated with a numeric choice number
    for index, choice in enumerate(choices, start=1):
        print(f'{index}) {choice}')
        # We store the choice in a dictionary for easy looking-up later
        options[str(index)] = choice  
    
    # Add a cancellation option if it was requested (default is False)
    if allow_cancellation:
        print('0) Cancel')
        options['0'] = None  # If the user does choose to cancel, we will return None
    
    # Simply loop until the user makes a valid selection
    user_input = input('Select an option: ')
    while user_input not in options.keys():
        print('Invalid selection')
        user_input = input('Select an option: ')
    
    # Look up the selected item and return it
    return options[user_input]

def clear():
    os.system('cls' if os.name =='nt' else 'clear')

def get_bundles(room_name)
    """ Returns a list of Bundle objects associated with a specific CommunityCenterRoom object """
    pass

def get_items(room_name)
    """ Returns a list of Item objects associated with a specific Bundle object """
    pass

def get_room_names():
    """ Retruns list of room names """
    room_names = []
    rooms = get_all_rooms()
    for room in rooms:
        room_names.append(room.name)
    return room_names
        
def view_bundles(room_name):
    """ View list of Bundles in a specific room""" 
    pass


def view_items(bundle_name):
    """ View bundle items """

    pass

def menu_loop():
    """ Show the main menu """
    
    print("Welcome to the Stardew Valley Community Center Bundle Tracker!")
    print('*' * 40)
    print("Please select a room")
    user_input = show_menu(view_rooms(), allow_cancellation=True)
    view_bundles(user_input)

#menu_loop()

