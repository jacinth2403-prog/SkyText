# SkyText

A weather-aware, multilingual literary recommendation assistant.

SkyText looks at the current weather (rainy, sunny, cloudy, etc.) and recommends
a poem, quote, or haiku that matches the mood — in English, Tamil, or Japanese —
along with an AI-generated explanation of why it fits.

## How it works
1. **Weather** — fetches current conditions from the OpenWeatherMap API.
2. **Retrieval** — matches the weather/mood to the most relevant poem using
   multilingual embeddings + a vector search (FAISS).
3. **Explanation** — Gemini generates a short, natural-language reason for
   the match.
4. **Frontend** — a simple Streamlit app ties it all together.

## Project structure
SkyText/
├── data/ # Poem/quote/haiku collection + metadata
├── embeddings/ # Scripts to build embeddings + vector store
├── weather/ # Weather API integration
├── llm/ # Gemini explanation logic
├── app/ # Streamlit frontend
├── requirements.txt
└── .env.example
## Setup (each teammate)
1. Clone the repo and move into it.
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your own API keys.
   - Free weather key: https://openweathermap.org/api
   - Free Gemini key: https://aistudio.google.com/apikey
4. Never commit your real `.env` file.

## Team
- Data collection & tagging: TBD
- Retrieval backend (weather + embeddings): TBD
- LLM layer & frontend: TBD
