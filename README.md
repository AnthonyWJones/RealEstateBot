# Real Estate Chatbot

A FastAPI-powered AI chatbot that assists users with real estate inquiries, such as answering property-related questions and providing general assistance.

---

## Features

- AI-powered chatbot using GPT-4o
- FastAPI backend for handling requests
- Simple API integration for frontend usage
- CORS support for web-based applications
- Basic frontend with index.html for chatbot interaction

---

## Project Structure
```
real_estate_bot/
│── main.py        # FastAPI application
│── .env           # API key
│── index.html     # Frontend for chatbot UI
└── README.md      # Documentation
```

---

## Installation & Setup

### 1. Clone the Repository
```
git clone https://github.com/AnthonyWJones/RealEstateBot.git
cd real_estate_bot
```

### 2. Create a Virtual Environment
```
python -m venv .venv
source .venv/bin/activate  # On Mac/Linux

# OR

.venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```
pip install fastapi uvicorn openai python-dotenv
```

### 4. Set Up Environment Variables

Create a .env file in the project directory and add your OpenAI API key:

```
OPENAI_API_KEY=your-openai-api-key-here
```

### 5. Run the Server
```
uvicorn main:app --reload
```

The API will now be available ```at http://127.0.0.1:8000```.

---

## API Endpoints

### Chatbot Endpoint

POST /chat  
Send a message to the AI bot.

Example Request:
```
{
  "message": "Tell me about real estate trends in my area."
}
```
Example Response:
```
{
  "reply": "The current real estate market trends suggest an increase in housing demand..."
}
```
---

## License

This project is licensed under the MIT License.

---

## Author

Anthony W. Jones  
tonybilljones@gmail.com
