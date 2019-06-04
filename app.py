# -*- coding: Utf-8 -*

from flask import Flask, render_template, request, jsonify

# Import of classes and functions
from application.parser import Parser
from application.place_search import PlaceSearch
from application.wiki_summary import WikiSummary
from application.message_generator import random_msgs

# Import of constants
from application.constants import APP_STOP_WORDS
from application.constants import INSUFFICIENT_INPUT_MSGS
from application.constants import START_SEARCH_MSGS
from application.constants import NO_LOCATION_MSGS
from application.constants import LOCATION_FOUND_MSGS
from application.constants import WIKIPEDIA_INTRO_MSGS
from application.constants import SHOW_OFF_MSGS
from application.constants import WIKIPEDIA_NOT_FOUND

# Import of API KEY, see README for more informations
from application.api_key import API_KEY

app = Flask(__name__)

# Initialization of classes
parsing = Parser(APP_STOP_WORDS)
place_search = PlaceSearch(API_KEY)
wiki_summary = WikiSummary()

# Route for AJAX request handling
@app.route('/_get_json')
def get_json():
    user_input = request.args.get("question", type=str)
    parsed_input = parsing.parsing_into_google_url(user_input)

    # Case if parsing function cut all words, input is then empty
    if len(parsed_input) == 0:
        return jsonify(message1=random_msgs(INSUFFICIENT_INPUT_MSGS),
                       error=True)

    # Case if at least one word comes out of the parsing
    else:
        location_dict = place_search.localize(parsed_input)

        # Case if Google doesn't find a corresponding place
        if location_dict == "No result found":
            return jsonify(message1=random_msgs(NO_LOCATION_MSGS),
                           error=True)

        # Case if Google found something
        else:
            address = location_dict["address"]
            longitude = location_dict["longitude"]
            latitude = location_dict["latitude"]

            # Work around the IndexError caused by Wikipedia module (no find)
            try:
                summary_search = wiki_summary.summary_of_place(location_dict)
                summary = summary_search.get('summary')
                url = summary_search.get('required_url')
                return jsonify(message1=random_msgs(LOCATION_FOUND_MSGS),
                               message5=address, 
                               message2=random_msgs(WIKIPEDIA_INTRO_MSGS),
                               message3=summary,
                               url=url,
                               message4=random_msgs(SHOW_OFF_MSGS),
                               longitude=longitude,
                               latitude=latitude,
                               error=False)
            except IndexError:
                return jsonify(message1=random_msgs(LOCATION_FOUND_MSGS),
                               message5=address, 
                               message2="",
                               message3=random_msgs(WIKIPEDIA_NOT_FOUND),
                               message4=random_msgs(SHOW_OFF_MSGS),
                               longitude=longitude,
                               latitude=latitude,
                               error=False)

@app.route('/')
def home():
    return render_template('home.html', api_key=API_KEY)

if __name__ == "__main__":
    app.run()