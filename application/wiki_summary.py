# -*- coding: Utf-8 -*

# Module with documentation at the following link :
# https://pypi.org/project/wikipedia/
import wikipedia

class WikiSummary:

    def __init__(self):
        """
        Since users are french speaking, set fr gives better results
        """
        wikipedia.set_lang("fr")

    def summary_of_place(self, localization_dict):
        """
        Require the dictionnary created by the place_search class,
        return a short summary
        """
        longitude = localization_dict.get("longitude")
        latitude = localization_dict.get("latitude")
        wikisearch = wikipedia.geosearch(latitude, longitude, results=1,
                                                              radius=100)
        anecdote = wikipedia.summary(wikisearch[0], sentences=2)
        location_for_url = wikipedia.page(wikisearch[0])
        required_url = location_for_url.url
        
        """ 
        Here a little workaround when wikipedia' summary is too short and there 
        is a title of a category, between ==, that appears. We want to delete 
        at this point
        """
        anecdote = anecdote.split()
        for i in anecdote:
            if i == "==":
                del anecdote[anecdote.index(i):]

        summary = " ".join(anecdote)

        return {
            "summary" : summary,
            "required_url" : required_url
        }
