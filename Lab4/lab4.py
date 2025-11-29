from strands import Agent, tool
from ddgs import DDGS # duckduckGo open APIs for search
from ddgs.exceptions import RatelimitException
import logging

logging.getLogger("strands").setLevel(logging.INFO)

@tool
def web_search(keywords:str, region: str = "en-in", maxResults: int | None = None) -> str:
    """
        Search the web to get updated information.
        Arguments:
            keywords: the serach query keywords.
            region: the search region: us-en, wt-wt, etc..
            maxResults: the maximum number of results to return in the query response.
        Returns:
            List of dictionaries with search results
    """

    try:
        results = DDGS().text(keywords, region=region, max_results=maxResults)
    except RatelimitException as rle:
        return f"RateLimitException, try after sometime {rle}"
    except Exception as e:
            return f"exception: {e}"

local_agent = Agent(system_prompt="""
        You're a recipe bot who has very good knowledge of indian cuisine.
        Help used with ingredients, cooking instructions and helpful links.
        Use the tools provided to you for better recommendations.
    """,
    tools = [web_search])

response = local_agent("Provide some recipe to make punjabi Rajma chawal")


print(f"Metrics : {response.metrics}") # publish token usage metrics