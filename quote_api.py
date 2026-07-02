import requests

class QuoteAPI:
    def __init__(self):
        self.URL = "https://dummyjson.com/quotes/random"



    def fetch_quotes(self):
        try:
            response = requests.get(self.URL, timeout=5)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.HTTPError as err:
            return f"ERROR : HTTP ERROR OCCURRED : {err}"
        except requests.exceptions.ConnectionError:
            return "ERROR : COULD NOT CONNECT TO THE API. CHECK YOUR INTERNET."
        except requests.exceptions.Timeout:
            return "ERROR : THE API REQUEST TIMED OUT."
        except Exception as error:
            return f"ERROR : AN UNEXPECTED ERROR OCCURRED: {error}"