from tkinter import *
from quote_ui import QuoteUi
from quote_logic import QuoteLogic

class MainController:
    def __init__(self):
        self.canvas = Tk()
        self.quote_logic = QuoteLogic()
        self.quote_ui = QuoteUi(self.canvas)
        self.quote_ui.labels()
        self.quote_ui.buttons()
        self.quote_ui.arrange_layout()
        self.connection()
        self.canvas.mainloop()


    def new_quote(self):
        result = self.quote_logic.fresh_quote()

        if self.quote_logic.error is not None:
            self.quote_ui.status_label.config(text=self.quote_logic.error, fg="red")
            self.quote_ui.status_label.pack()
        else:
            self.quote_ui.status_label.config(text="")
            self.quote_ui.status_label.pack_forget()

        if  isinstance(result, str):
            self.quote_ui.quote_label.config(text=result)
            self.quote_ui.author_label.config(text="")
        else:

            quote_text = f'“{result["quote"]}”'
            #quote_id = result["id"]
            quote_author = f"— {result['author']}"
            self.quote_ui.quote_label.config(text= quote_text)
            self.quote_ui.author_label.config(text= quote_author)

    def connection(self):
        self.quote_ui.new_quote.config(command = self.new_quote)

controller = MainController()