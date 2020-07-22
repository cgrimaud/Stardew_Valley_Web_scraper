from bs4 import BeautifulSoup
import pickle
import requests
from sdv_classes import Bundle, CommunityCenterRoom, Item
# needed for OrderedDict
from collections import OrderedDict
# needed to clear screen
import os
import time

### Scrape page, parse data into list of objects ###

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
            bundle_items = []
            if "Quality" not in bundle_name:
                rows = table.find_all('td')   
                for row in rows[2:-2:2]:
                    item_name = row.text.lstrip()
                    item_object = Item(item_name)
                    bundle_items.append(item_object)
            else:
                rows = table.find_all('td')
                for row in rows:
                    tbl_row = row.find_all('table')
                    for tbl in tbl_row:
                        item_name = tbl.text.lstrip() + '\n'
                        item_object = Item(item_name)
                        bundle_items.append(item_object)
                        

            # Gets number of required items to complete bundle
            required_items = 0    
            for row in rows[1].find_all(recursive=False):
                if row:
                    required_items += 1
        
            # create Bundle objects and append objects to a list
            bundle_object = Bundle(bundle_name, required_items, cc_room, bundle_items)
            bundles.append(bundle_object)

    return bundles

def pickle_rooms_to_file():
    rooms = get_all_rooms()
    pickle_out = open('rooms', "wb")
    pickle.dump(rooms, pickle_out)
    pickle_out.close()


#### Functions working with list of objects ###

def clear():
    """ clears the console """
    os.system('cls' if os.name =='nt' else 'clear')

def get_room_bundles(room_name):
    """ Returns a list of Bundle objects associated with a specific CommunityCenterRoom object
    Parameters: 
        room_name: name of CommunityCenterRoom Object
    Returns:
        room_bundles list: a list of Bundle objects associated with the CommunityCenterRoom passed in
    """
    # open and load rooms file
    pickle_in = open("rooms", 'rb')
    rooms = pickle.load(pickle_in)
    bundles = []
    for room in rooms:
        if room.name == room_name:
            bundles.append(room.bundles)
    pickle_in.close()
    # list comprehension to flatten bundles list  
    room_bundles = [item for sublist in bundles for item in sublist]
    return room_bundles
    
def get_bundle_items(room_name, bundle_name):
    """ Returns a list of Item objects associated with a specific Bundle object
    Parameters: 
        room_name: name of CommunityCenterRoom Object
        bundle_name: name of Bundle object inside of the CommunityCenterRoom Object
    Returns:
        bundle_items list: a list of Item objects associated with the Bundle object passed in
    """
    
    bundles = get_room_bundles(room_name)
    items = []
    for bundle in bundles:
        if bundle.name == bundle_name:
            items.append(bundle.items)
    bundle_items = [item for sublist in items for item in sublist]
    return bundle_items

def get_names(obj_list):
    """ Retruns list of names
    Parameters: 
        obj_list: list of objects where there objects have 'name' as an attribute
    Returns:
        names list: list of the name attributes in the obj_list
    """
    names = []
    for obj in obj_list:
        names.append(obj.name)
    return names
        

### Menus ### 

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
        print('0) Exit')
        options['0'] = None  # If the user does choose to cancel, we will return None
    else:
        print('0) Return to Main Menu')
        options['0'] = None  
    
    # Simply loop until the user makes a valid selection
    user_input = input('Select an option: ')
    while user_input not in options.keys():
        print('Invalid selection')
        user_input = input('Select an option: ')
    
    # Look up the selected item and return it
    return options[user_input]

def room_menu():
    """ Show the main menu """
    
    pickle_in = open("rooms", 'rb')
    rooms = pickle.load(pickle_in)

    clear()
    print("Welcome to the Stardew Valley Community Center Bundle Tracker!")
    print('*' * 60)
    print("Please select a room")
    print('-' * 25)
    user_selected_room = show_menu(get_names(rooms), allow_cancellation=True)
    if user_selected_room == None:
        pickle_in.close()
        exit()
    else:
        bundle_menu(user_selected_room)

def bundle_menu(room):
    """ Show menu of bundles in a specific room """

    # Vault bundles == items so vault object doesn't have items
    if room == "Vault":
        clear()
        print("***", room, "***")
        print("Please select the bundle you've completed")
        print('-' * 25)
        user_selected_bundle = show_menu(get_names(get_room_bundles(room)), allow_cancellation=False)
        while user_selected_bundle is not None:
            room_bundles = get_room_bundles(room)
            for bundle in room_bundles:
                if user_selected_bundle == bundle.name:
                    print(f'{bundle.name} has been donated!')
                    time.sleep(1)
                    clear()
                    print("***", room, "***")
                    print("Please select the bundle you've completed")
                    print('-' * 25)
                    user_selected_bundle = show_menu(get_names(get_room_bundles(room)), allow_cancellation=False)
        else:
            room_menu()

    else: 
        clear()
        print("***", room, "***")
        print("Please select a bundle")
        print('-' * 25)
        user_selected_bundle = show_menu(get_names(get_room_bundles(room)), allow_cancellation=False)
        if user_selected_bundle == None:
            room_menu()
        else:
            item_menu(room, user_selected_bundle)    

def item_menu(room, bundle):
    """ Show menu of items in a specific bundle """

    clear()
    print("***", bundle, "***")
    print("Select the item you've donated to the Community Center")
    print('-' * 55)
    user_selected_item = show_menu(get_names(get_bundle_items(room, bundle)), allow_cancellation=False)
    while user_selected_item is not None:
        bundle_items = get_bundle_items(room, bundle)
        for item in bundle_items:
            if user_selected_item == item.name:
                print(f"You've donated the {item.name}")
                time.sleep(1)
                clear()
                print("***", bundle, "***")
                print("Select the item you've donated to the Community Center")
                print('-' * 55)
                user_selected_item = show_menu(get_names(get_bundle_items(room, bundle)), allow_cancellation=False)
    else:
        room_menu()

pickle_rooms_to_file()
room_menu()

