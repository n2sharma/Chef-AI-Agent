import logging
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from photo_decoder import build_image_message, choose_image_file
from prompt import CHEF_PROMPT, SYSTEM_CHEF_PROMPT
from tools import web_search

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
load_dotenv()

# Any vision-capable + tool-calling model on OpenRouter works here.
# Examples: "openai/gpt-5-nano", "google/gemini-2.5-flash", "anthropic/claude-sonnet-4.5"
MODEL_NAME = os.getenv("OPENROUTER_MODEL", "google/gemini-2.5-flash")


def main() -> None:
    logging.info("creating our agent...")
    model = ChatOpenAI(
        model=MODEL_NAME,
        api_key=os.environ["OPENROUTER_API_KEY"],
        base_url="https://openrouter.ai/api/v1",
    )
    agent = create_agent(
        model=model,
        tools=[web_search],
        system_prompt=SYSTEM_CHEF_PROMPT,
    )

    logging.info("choosing our image...")
    path = choose_image_file()
    message = build_image_message(path, CHEF_PROMPT)

    logging.info("invoking our agent...")
    try:
        response = agent.invoke({"messages": [message]})
    except Exception as e:
        logging.error("Agent failed: %s", e)
        raise SystemExit(1)

    print(response["messages"][-1].content)


if __name__ == "__main__":
    main()