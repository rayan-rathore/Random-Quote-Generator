# 📖 Random Quote Generator

A simple yet well-structured Python desktop application that fetches random inspirational quotes from an online API and stores them locally for offline access. The project follows a modular design using Object-Oriented Programming (OOP) principles and separates the application's API, business logic, user interface, and controller into different modules.

---

## 📌 Overview

Random Quote Generator is a desktop application built with **Python** and **Tkinter** that allows users to discover inspiring quotes with a single click.

Whenever a user requests a new quote, the application fetches one from the online API. Every unique quote is automatically saved into a local JSON file, creating a growing offline collection. If the internet connection becomes unavailable, the application seamlessly switches to the locally stored quotes, ensuring it remains functional even without network access.

The project was developed to practice:

* Object-Oriented Programming (OOP)
* API integration
* JSON data handling
* Exception handling
* File management
* GUI development with Tkinter
* Modular project architecture

---

# ✨ Features

* 🎲 Fetches a random quote from an online API.
* 💾 Automatically saves new quotes locally.
* 🔄 Prevents duplicate quotes from being stored.
* 🌐 Handles internet connection failures gracefully.
* 📂 Uses cached quotes when offline.
* 🖥️ Clean and responsive Tkinter interface.
* ⚠️ Displays meaningful error messages.
* 📦 Organized into multiple modules for maintainability.

---

# 📸 Screenshot

<img width="1919" height="1079" alt="Screenshot 2026-07-02 070055" src="https://github.com/user-attachments/assets/15425a9d-0566-45e9-ba14-15996da0e802" />
<img width="1919" height="1079" alt="Screenshot 2026-07-02 070016" src="https://github.com/user-attachments/assets/5c4c816c-78e3-4ffc-9bad-05c6e50a679c" />
<img width="1919" height="1079" alt="Screenshot 2026-07-02 065940" src="https://github.com/user-attachments/assets/da3e4edd-dd7f-40be-b964-594b5455628e" />
<img width="1919" height="1079" alt="Screenshot 2026-07-02 065858" src="https://github.com/user-attachments/assets/fa8580fb-9938-451f-b368-9824dafa15b2" />


---

# 🏗 Project Structure

```text
Random-Quote-Generator/
│
├── quote_api.py          # Handles API requests
├── quote_logic.py        # Business logic
├── quote_ui.py           # Tkinter user interface
├── main_controller.py    # Main controller
├── random_quotes.json    # Local quote database
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙️ Technologies Used

* Python 3
* Tkinter
* Requests
* JSON
* Object-Oriented Programming (OOP)

---

# 📚 How It Works

The application follows a simple workflow.

1. The user clicks **Discover Quote**.
2. The application sends a request to the online API.
3. If the request succeeds:

   * The quote is displayed.
   * Duplicate quotes are ignored.
   * New quotes are saved locally.
4. If the request fails:

   * The application loads a previously saved quote from the local JSON file.
5. If no local quotes exist, an appropriate message is shown.

---

# 🧩 Application Architecture

The project follows a modular architecture that separates responsibilities into different components.

## 1. QuoteAPI

Responsible for communicating with the external API.

Responsibilities:

* Send HTTP requests
* Handle API errors
* Return quote data

---

## 2. QuoteLogic

Acts as the business layer.

Responsibilities:

* Fetch quotes
* Load local JSON data
* Detect duplicates
* Save new quotes
* Handle offline mode

---

## 3. QuoteUI

Responsible only for the graphical interface.

Responsibilities:

* Create labels
* Create buttons
* Arrange widgets
* Display quote information

---

## 4. MainController

Acts as the controller that connects everything together.

Responsibilities:

* Handle button events
* Update UI
* Display error messages
* Coordinate communication between the UI and business logic

---

# 🌐 API Used

The application uses the DummyJSON Quotes API.

Endpoint:

```
https://dummyjson.com/quotes/random
```

Each request returns a random quote in JSON format.

Example response:

```json
{
    "id": 13,
    "quote": "The future depends on what you do today.",
    "author": "Mahatma Gandhi"
}
```

---

# 💾 Local Storage

Every unique quote retrieved from the API is stored in:

```
random_quotes.json
```

This file acts as a small offline database.

Benefits:

* Offline support
* Faster access
* Duplicate prevention
* Persistent storage

---

# 🛡 Error Handling

The application handles several possible errors.

* HTTP errors
* Connection errors
* Timeout errors
* Invalid JSON files
* Missing local storage file
* Unexpected exceptions

Instead of crashing, the application displays a meaningful message and attempts to use locally stored quotes whenever possible.

---

# 🚀 Installation

## Clone the repository

```bash
git clone https://github.com/yourusername/Random-Quote-Generator.git
```

Move into the project directory.

```bash
cd Random-Quote-Generator
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
python main.py
```

---

# 📦 Requirements

```
requests
```

or install using

```bash
pip install requests
```

---

# 🎯 Learning Outcomes

This project helped me practice and understand:

* Python classes and objects
* Modular programming
* Separation of concerns
* REST API integration
* JSON serialization
* Exception handling
* File operations
* Tkinter GUI development
* Basic MVC-style architecture
* Offline-first application design

---

# 🔮 Future Improvements

Possible enhancements include:

* Quote categories
* Search by author
* Favorite quotes
* Copy quote to clipboard
* Export quotes
* Dark and light themes
* Quote history
* Random background colors
* Keyboard shortcuts
* Better UI styling using ttk
* Packaging as a standalone executable

---

# 🤝 Contributing

Contributions, ideas, and suggestions are welcome.

If you'd like to improve the project:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

