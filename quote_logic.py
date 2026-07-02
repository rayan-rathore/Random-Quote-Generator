import json
import random

from quote_api import QuoteAPI

class QuoteLogic:
    def __init__(self):
        self.data = QuoteAPI()
        self.error = None


    def fresh_quote(self):
        quote = self.data.fetch_quotes()

        try:
            with open("random_quotes.json", mode="r", encoding="utf-8") as file:
                existing_file = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_file = []


        if not isinstance(quote, dict):
            self.error = quote
            if len(existing_file) > 0:
                return random.choice(existing_file)
            else:
                return "No quote is available!"

        self.error = None

        is_duplicate = False
        for saved_quote in existing_file:
            if quote["id"] ==  saved_quote["id"]:
                is_duplicate = True

        if not is_duplicate:
            existing_file.append(quote)
            with open("random_quotes.json", mode="w", encoding="utf-8") as file:
                json.dump(existing_file, file,indent=4)
        return quote


