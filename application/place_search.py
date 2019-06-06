# -*- coding: Utf-8 -*

# Path precision for Pytest purposes
import sys
sys.path.append('..')

import requests
import json


class PlaceSearch:

    def __init__(self, api_key):
        """ 
        API key must be provided.
        No API key available in the source code.
        """
        self.api_key = api_key

    def google_place_search_api(self, parsed_user_input):
        """ 
        Link with google place search to find the adress and geographical 
        coordinates. We set the research in French for better accuracy.
        """  
        research_url = 'https://maps.googleapis.com/maps/api/place/findplacefro\
mtext/json?input=%s&inputtype=textquery&language=fr&fields=formatted_address,na\
me,geometry&key=%s' % (parsed_user_input, self.api_key)

        r = requests.get(url=research_url)
        data_dict = r.json()
        data = data_dict.get("candidates")

        return data

    def localize(self, parsed_user_input):
        """ 
        Extraction of adress, lat and long values
        """

        data = self.google_place_search_api(parsed_user_input)

        if len(data) >= 1:
            address = data[0].get("formatted_address")

            #t_ means those variables are of temporary use within this function
            t_geometry = data[0].get("geometry")
            t_location = t_geometry.get("location")

            longitude = t_location.get("lng")
            latitude = t_location.get("lat")
            return {
                "address" : address,
                "longitude" : longitude,
                "latitude" : latitude
            }

        else:
            return "No result found"