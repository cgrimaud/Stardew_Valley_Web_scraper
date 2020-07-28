# Stardew Valley Webscraper

Stardew Valley is an open-ended country-life RPG. One part of the game is the option to restore the dilapidated Community Center building by donating specific items. 

This program scrapes https://stardewvalleywiki.com/Bundles and allows the user view Community Center Rooms, Bundles in those rooms, and donatable Items inside of those bundles all via the command line. 

 

## How to Run:
This program was written in Python 3.8 and utilizes Pipenv to implement non-native libraries. 

* Make sure you have Python 3.8

Clone or Download the project and open it in Visual Studio Code. 
Open a New Terminal and type the following in the command line to install pipenv:

```pip install pipenv```

Then install the packages associated with the project by running:

```pipenv install```

Finally, run the project by typing:

```pipenv run python bundle_scraper.py```


## What to expect:
The first menu will be a list of all of the Rooms inside of the Community Center. From here, you can either select 0 to exit the program or select a room:

![image](https://user-images.githubusercontent.com/44476865/88121998-64354600-cb95-11ea-941a-b05290c937ab.png)

When you select a room, a list of bundles associated with that room will appear. You can select a specific bundle or select 0 to return to the main menu:

![image](https://user-images.githubusercontent.com/44476865/88122608-11f52480-cb97-11ea-841a-8ac2832849fe.png)

If you select a sepcific bundle, a list of donatable items associated with that bundle will appear. From here you can select items to "donate":

![image](https://user-images.githubusercontent.com/44476865/88122699-436df000-cb97-11ea-8f33-12233aae588c.png)

### Functionality Notes/Exceptions:
  * The Vault Room (option 6 in the main menu) does not have an Items menu. The bundles are the items, therefore they can be "donated" at the bundle level
  * While the program lets the user select items to "donate" there is no true functionality tied to this action at this time (other than a brief note to the user in the menu). This will be addressed in future iterations of this project. 

## CL Requirements Met:

#### 5+ Commits on Github

#### Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program

#### Create a class, then create at least one object of that class and populate it with data
I've created three classes as seen in [sdv_classes.py](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/sdv_classes.py).
* [Instances of CommunityCenterRoom](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L35) are created in the parse_rooms() function     
* [Instances of Bundle](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L79) and [instances of Item](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L56-L69) are created in the parse_room_bundles() function

#### Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program
Lists are used throughout the program. 
* [parse_rooms()](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L24-L36) & [parse_room_bundles()](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L38-L82) work together to create a complete list of CommunityCenterRoom Objects from the webscraped data (as well as using lists inside of the functions themselves).
* [get_room_bundles()](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L97-L114), [get_bundle_items()](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L116-L131), & [get_names()](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L133-L143) each return lists which are utilized in the different menu functions. 


#### Read data from an external file, such as text, JSON, CSV, etc and use that data in your application
The program first scrapes the Stardew Valley Wiki then [saves the parsed data to a file](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L84-L88) named rooms. That file is then opened and read in the "Functions working with list of objects" section of the code (specifically [here](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L104-L106) & [here](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L183-L184)). 

#### Create and call at least 3 functions, at least one of which must return a value that is used
* [parse_rooms()](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L24-L36) returns a list of CommunityCenterRoom objects and is called in [get_all_rooms()](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L22)

* [parse_room_bundles()](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L38-L82) returns a list of Bundle Objects associated with a community center room and is called in [parse_rooms()](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L34)

* [get_room_bundles()](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L97-L114) returns a list of Bundle objects associated with the CommunityCenterRoom passed in and is called in [get_bundle_items()](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L125) & [bundle_menu()](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L207-L227)

* [get_bundle_items()](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L116-L131) returns a list of Item objects associated with the Bundle object passed in and is called in [item_menu()](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L240-L251)

* [get_names()](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L133-L143) returns a list of names and is called in [room_menu()](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L191), [bundle_menu()](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L207-L227), & [item_menu()](https://github.com/cgrimaud/Stardew_Valley_Web_scraper/blob/ad2ded4e1f9b9f2b9a203667ce675fa8ff9d14b9/bundle_scraper.py#L240-L251) any time show_menu() is called. 
