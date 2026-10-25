import logging
import os
from typing import Any, Dict

from langchain.tools import tool
from tavily import TavilyClient


@tool
def web_search(query: str) -> Dict[str, Any]:
    """Search the web for information, such as recipes."""
    logging.info("searching for %s", query)
    client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
    return client.search(query)
