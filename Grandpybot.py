from flask import Flask, render_template, request, jsonify

from application.parser import Parser
from application.place_search import PlaceSearch
from application.wiki_summary import WikiSummary

from application.constants import APP_STOP_WORDS

app = Flask(__name__)

parsing = Parser(APP_STOP_WORDS)
place_search = PlaceSearch("APIKEY")
wiki_summary = WikiSummary()

@app.route('/_get_json')
def get_json():
    user_input = request.args.get("question", type=str)
    parsed_input = parsing.parsing_into_google_url(user_input)
    if len(parsed_input) == 0:
        return jsonify(message1="je n'ai pas compris", error=True)
    else:
        localization_dict = place_search.localize(parsed_input)
        
        if localization_dict == "No result found":
            return jsonify(message1="désolé gamin j'ai rien trouvé", error=True)
        else:
            adress = localization_dict["adress"]
            longitude = localization_dict["longitude"]
            latitude = localization_dict["latitude"]
            return jsonify(message1=adress, longitude=longitude, latitude=latitude, error=False)




@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)