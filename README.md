# Project7_OC
Repository for the 7th project of Open Classrooms (PYTHON), named GrandPy Bot.

Goal of this project is to create a website with a back-end application that simulate a bot which can give the address and some facts about a place indicated by the user, as well as displaying a map with a marker on the place.

Note that the application is made for French speakers, sentences in english will not be correctly parsed and might be misinterpreted by a critical function of the programm. 

# VERSION 1.2

Third functional version of the application, second to be deployed online. 

Website link : https://vd-grandpybot-p7.herokuapp.com/

# WHAT'S NEW

Minor fixes and add of Wikipedia link when a request is successful.

# HOW TO TEST THE APPLICATION

To test the existing code, please follow these instructions :

1) Install the dependencies with the requirements.txt file

2) Obtain your own Google API Key and create a file in the application folder called api_key.py and inside create a variable called API_KEY containing a string of your api key.

3) Run the main file (Grandpybot.py) and access the page with the browser at localhost adress.

NOTE : Since there are use of CDNs, you need a internet connection to ensure a proper display (bootstrap), or simply to have answers from wikipedia or Google.

# KNOWN BUGS AND NECESSARY IMPROVEMENTS

The followings items are actively looked upon and will be fixed really soon :
- Although the programm is simulating a conversation, the lack of temporality (i.e all the answers given exactly together) make it clunky, might need to add some milliseconds of delay between each sentence.
- Chat box needs to be auto-scrolled when reaching the bottom.

# SPECIAL THANKS

I would like to express my deepest thanks to Elia Benfatto (https://github.com/EliaTB). He doesn't know me and I don't know him personnaly, but we share the same school mentor. When I was completely lost within my own code, our mentor gave me his version which was doing exactly the same thing as mine, but everything was cleaner, prettier and so much more understandable. It forced my to begin anew and transform my previous spaghetti code into something I am way more proud of, learning many things in the process. Thanks again !


