# -*- coding: Utf-8 -*

# Built-in for splitting sentences with multiple separators
import re

# Path precision for pytest
import sys
sys.path.append('..')


class Parser:
    """ Class to operate the parsing of user input """
    def __init__(self, stop_words):
        self.stop_words = stop_words

    def parsing_into_google_url(self, user_input):
        """ Parse the user input and transform it in URL google friendly """
        if user_input == "":
            parsed_user_input = None
            return parsed_user_input
        else:
            user_input_lowered_case = user_input.lower()
            list_sentence_split = re.split("[' , ?]", user_input_lowered_case)
            list_parsed_sentence = []
            for i in list_sentence_split:
                if i not in self.stop_words:
                    list_parsed_sentence.append(i)
            parsed_user_input = "%20".join(list_parsed_sentence)
            return parsed_user_input
