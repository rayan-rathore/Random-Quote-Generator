from tkinter import *

class QuoteUi:
    def __init__(self, window):
        self.window = window
        self.w_size = window.geometry("600x450")
        self.window.title("Random Quote Generator")

        self.BG_COLOR = "#1E1E2E"
        self.CARD_COLOR = "#252538"
        self.TEXT_COLOR = "#C6D0F5"
        self.AUTHOR_COLOR = "#8CAAEE"
        self.BUTTON_BG = "#303446"

        self.window.config(bg=self.BG_COLOR)

        self.author_label = None
        self.quote_label = None
        self.status_label = None
        self.new_quote = None



    def labels(self):
        self.quote_label = Label(self.window,text="Click the button below to fetch an inspiring quote.",
                                 font=("Georgia", 16, "italic"),
                                 fg=self.TEXT_COLOR,bg=self.BG_COLOR,wraplength=450,justify="center")
        self.author_label = Label(self.window, text="", font=("Arial", 12, "bold")
                                  ,fg=self.AUTHOR_COLOR,bg=self.BG_COLOR)
        self.status_label = Label(self.window, font=("Arial", 10,"bold"),fg= "#E64553",
                                  bg=self.BG_COLOR,)



    def buttons(self):
        self.new_quote = Button(self.window, text="Discover Quote", font=("Arial", 12, "bold"),
                                fg= "#FFFFFF",bg= "#00FF00",activebackground=self.AUTHOR_COLOR,
                                 activeforeground="#1E1E2F",bd=0,padx=20,pady=10,cursor="hand2" )

    def arrange_layout(self):
        self.quote_label.pack(expand=True, fill="both", padx=40, pady=(40, 10))
        self.author_label.pack(pady=(0, 30))
        self.new_quote.pack(pady=(0, 20))
        self.status_label.pack(pady=(0, 15))
