# FastEat

A LangChain agent that takes a photo of your ingredients, identifies them with a vision LLM (via OpenRouter), searches the web with Tavily for a recipe that uses only those ingredients, and prints it.

## Setup

```sh
uv sync
cp .env.example .env   # then fill in OPENROUTER_API_KEY and TAVILY_API_KEY
```

## Run

```sh
uv run main.py
```

A file picker opens to choose an image (if no display is available, you're prompted for a path instead).

## Change the model

Set `OPENROUTER_MODEL` in `.env` (default: `google/gemini-2.5-flash`). It must support image input and tool calling, e.g. `openai/gpt-5-nano` or `anthropic/claude-sonnet-4.5`.
