# -*- coding: Utf-8 -*

import sys
sys.path.append('..')

import json
import requests

from application.place_search import PlaceSearch

place_search = PlaceSearch('api_key')

def mock_google_place_search_api(self, input):
    data = [
        {
            "formatted_address" : "Rue du Gros Horloge, 76000 Rouen, France",
            "geometry" : {
                "location" : {
                    "lat" : 49.4415381,
                    "lng" : 1.0912618
                },
                "viewport" : {
                    "northeast" : {
                        "lat" : 49.44286327989273,
                        "lng" : 1.092590629892722
                    },
                    "southwest" : {
                        "lat" : 49.44016362010728,
                        "lng" : 1.089890970107278
                    }
                }
            },
            "name" : "Le Gros-Horloge"
        }
    ]

    return data

def test_localize(monkeypatch):
    monkeypatch.setattr(PlaceSearch, 'google_place_search_api', mock_google_place_search_api)
    result = place_search.localize('input')
    assert result["address"] == "Rue du Gros Horloge, 76000 Rouen, France"
    assert result["longitude"] == 1.0912618
    assert result["latitude"] == 49.4415381
