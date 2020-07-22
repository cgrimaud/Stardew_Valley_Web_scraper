# Stardew Valley Webscraper

Stardew Valley is an open-ended country-life RPG. One part of the game is the option to restore the dilapidated Community Center building by donating specific 

This program scrapes https://stardewvalleywiki.com/Bundles and allows the user view Community Center Rooms, Bundles in those rooms, and donatable Items inside of those bundles all via the command line. 

This program was written in Python 3.8 and utilizes Pipenv to implement non-native libraries.  

## How to Run:
Clone or Download the project and open it in Visual Studio Code. 
Open a New Terminal and type the following in the command line:

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

* Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program

* Create a class, then create at least one object of that class and populate it with data

* Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program

* Read data from an external file, such as text, JSON, CSV, etc and use that data in your application

* Create and call at least 3 functions, at least one of which must return a value that is used
