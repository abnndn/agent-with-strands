from strands import Agent, tool

system_prompt = """
    You are just a standard basic model who's a jack of all trades.
"""

@tool
def word_count(text: str) -> int:
    """
    This method can count the number of words in a sentence.
    """

    return len(text.split())

local_agent = Agent(
    system_prompt = system_prompt,
    tools = [word_count]
)

local_agent("How many words are present in this sentence? - golbusa asdfa asdfash asdf ew sfs sdfsd")
