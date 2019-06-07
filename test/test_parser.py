# -*- coding: Utf-8 -*

import sys
sys.path.append('..')

from application.parser import Parser
from application.constants import APP_STOP_WORDS

parsing = Parser(APP_STOP_WORDS)

def test_parsing_into_google_url():
    assert parsing.parsing_into_google_url("") == None
    assert parsing.parsing_into_google_url("la") == ""
    assert parsing.parsing_into_google_url("la tour eiffel") == "tour%20eiffel"
    assert parsing.parsing_into_google_url("La Tour Eiffel") == "tour%20eiffel"
    assert parsing.parsing_into_google_url("Le Mont Saint-Michel") == "mont%20saint-michel"
    assert parsing.parsing_into_google_url("Abbaye aux hommes") == "abbaye%20hommes"
    assert parsing.parsing_into_google_url("l'Abbaye aux hommes") == "abbaye%20hommes"
    assert parsing.parsing_into_google_url("l'abbaye aux femmes, Caen") == "abbaye%20femmes%20caen"
    assert parsing.parsing_into_google_url("Salut GrandPy, tu peux me dire où se trouve le gros-horloge de Rouen?") == "gros-horloge%20rouen"