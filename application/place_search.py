# -*- coding: Utf-8 -*

#On précise le path sinon ça fait planter pytest
import sys
sys.path.append('..')

import requests
import json


class PlaceSearch:

    def __init__(self, api_key):
        self.api_key = api_key

    def localize(self, parsed_user_input):
        """ Link with google place search to find the adress and geographical coordinates """
        research_url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/\
json?input=%s&inputtype=textquery&language=fr&fields=formatted_address,name,geometry\
&key=%s' % (parsed_user_input, self.api_key)

        r = requests.get(url=research_url)
        data_dict = r.json()
        data = data_dict.get("candidates")

        if len(data) >= 1:
            address = data[0].get("formatted_address")

            #t_ means those variables are of temporary use within this function
            t_geometry = data[0].get("geometry")
            t_location = t_geometry.get("location")

            longitude = t_location.get("lng")
            latitude = t_location.get("lat")
            return {
                "adress" : address,
                "longitude" : longitude,
                "latitude" : latitude
            }

        else:
            return "No result found"