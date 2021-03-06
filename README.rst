===========================
Deep_Keyword_Searcher
===========================

An app that does a deep search for a keyword through folders, files, and zipped files.
  Written in Python!
    Yay! Go team Python!


Can search for a Keyword:
   - In file names.
   - In the text within a file.
   - In the text within a file that is inside a zipped file.
   - Can search through all sub directories of the directory you select for the search.
   - Can do case sensitive or case insensitive searches.
   - More options and usefulness than Windows file explorer keyword search.
   - Oddly, much faster than Windows file explorer keyword search when searching for only file or folder names.
       * Still don't know why it's faster.

Other features:
   - Lightweight easy to use GUI.
   - Fast
   - Results displayed in an intuitive Tree Structure.
   - In file text matches are displayed with a line number to help you locate it even more easily!
   - A right click menu for files and folders in the Tree Structure.
       * You can copy the directory path to the file or folder.
       * You can open a folder in file explorer.
       * You can open a file with the preferred application you have selected for that file type.

Works on Windows and Linux
==========================

Main Goal
=========
I didn't find any app on the internet like this app, but someone's got to do it
eventually, so I guess this time it was my turn to be THAT guy. LOL

I made this app while making mods for a game named Stellaris, by Paradox
Interactive. I wanted to be able to locate all occurrences of an object I was
going to modify. I found it very tedious to search through each file
manually, to the point that it was so much work, it just wasn't worth the effort.

For example: Let's say I was going to make some changes to a planet class
called pc_tropical, but I wanted to make sure my changes didn't break other
functionality related to the pc_tropical planet type, I would search for
"pc_tropical" with this app, and anaylze the code in files where the keyword
match was found and make changes or fixes where necessary.

I personally have found this app invaluable in my modding efforts for many games
now, and I can't even count how many hundreds of hours this app has saved me.

Though, it can be used for anything really. If you need to search through a large
amount of text in a multitude of files, located in different directories, then
this app can help you.

Example of Usage (Sorry for the huge images)
================
.. image:: https://i.imgur.com/zjjJFJR.png
.. image:: https://i.imgur.com/0gkyuor.png
.. image:: https://i.imgur.com/D5Nrdh7.png


Prerequisites
=============

Supports Python 3.x only.

Installation
============

There are a few different installation options I will provide you:


For WINDOWS:
===========

OPTION 1 EASY WAY:
   - Use the zip file in the releases section that contains the app already compiled using the PyInstaller library.
   - All you got to do is unzip it, and double click the shortcut to the executable.
   NOTE:  Since I have not purchased a certificate(cheapest I found was $84) to sign my applications with, the app will likely be detected by Anti-Virus software as possibly malicious. Until I scrounge up the money to pay for a certificate, this will likely be a continuing issue.
    
    If you don't feel comfortable taking using this option, I don't blame you. I suggest just downloading the .py files, which you can read through all the contents and verify that they're not malicious yourself, and use PyInstaller to compile it into an executable. Or just run it through command promt or powershell with Python. Or if you use Linux, you don't have to go through any of this trouble, and you can literally just execute the .py file right then and there, no need for a .exe.


OPTION 2 HARD WAY # 1 (Check Dependacies Section below):
   - Download Python 3.x and all the 3rd-party libraries used in the app, and then use PyInstaller yourself and compile it into an executable application yourself.
   - Download the zip with the .py files, and then follow the instructions THAT PyInstaller provides on how to turn .py files into an executable.
   - Just make sure that deep_keyword_searcher.py is in the same folder as deep_keyword_searcher_gui.py
   - Note that deep_keyword_searcher_gui.py is the GUI file, the deep_keyword_searcher.py is the file that does the heavy lifting.

OPTION 3 LESS HARD WAY, but not as easy as Option 1(Check Dependacies Section below):
   - Download Python and all the 3rd-party libraries used in the app, and run the app in powershell.
   - Download the zip with the .py files, with all the 3rd part libraries installed, just run the deep_keyword_searcher_gui.py file in powershell.
   - Just make sure that deep_keyword_searcher.py is in the same folder as deep_keyword_searcher_gui.py


For LINUX
==========
TWO OPTIONS:
   - Step one:
      * Fist off, congratulate yourself for using Linux!
   - Step two (Chose one):
      * Set the file to be executable. NOTE: Sometimes this doesn't work on a distro for some odd reason. Either that or I got something wrong with the executable functionality on my Kubuntu install.
   - OR
      * Right-click deep_keyword_searcher_gui.py and select "Run in Konsole"(Or whatever equivalent your distro has for that)
   - Just make sure that deep_keyword_searcher.py is in the same folder as deep_keyword_searcher_gui.py


Dependencies
============

- Python 3.x (Latest version is always reccommended)
- Python 3.x libraries(Make sure you download the Python 3.x versions)
    * pyperclip
    * ntpath

License
=======
This project is licensed under the MIT License.

See the LICENSE file for details.
 link: https://github.com/D-Chase-H/Deep_Keyword_Searcher/blob/master/LICENSE

TO-DO List (Will fix to these soon)
==========
- Change the id of the internal zipped file matches, so you can copy and paste the path or open the file.
- Fix some issues when searching on Linux from the root directory, or home.
- Fine a way to visually display a folder in the tree view, when there is a keyword match within the folder's name.

Planned Future Features
=======================
* Mac compatibility

Probably Going To Add Features
==============================
* The option to set a depth limit for how far it will search into sub-directories.
* Make the GUI look a little better. Maybe make some art to add to it.
* Make the ability to save a search to a file, and be able to load it up, so you don't have to do it again.(Assuming no files/folders were added/removed.)

Features That Might Be Added Eventually... Maybe... Possibly...
===============================================================
* Other search options, like different types of fuzzy search.


Donations
=========
Not that I ever expect any donations for the mods I make for games, but there are just some generous people out there and I am not going to turn away any appreciation someone wants to show, via their money.

Well, that same philosophy goes here too. I didn't make this app for money, but if you feel generous and want to donate, then here is a link to my PayPal donations account I have for my all game mod donations.

.. image:: https://i.imgur.com/gmaqOA3.png
   :target: https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=FDDF9FTVUQX4S&currency_code=USD&source=url

Credits
=======

This app was created by GitHub User, D-Chase-H.

    * My LinkedIn: www.linkedin.com/in/dustinchaseharmon

    * My HackerRanks.com Profile: https://www.hackerrank.com/CHarmon

Contributing
============
Under normal circumstances I should get to pull requests within a few hours or
by the next day. Bear with me if I can't get to your requests right away.

Please, send a pull request with your changes, and comments are appreciated.

Acknowledgments
===============

- A tip of the hat to all the open source third-party libraries used in
  this project!
- Thank you to all those who contribute with pull requests!
