# gpt_generator.py
import openai
import logging


# Configuring logging 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def run(tokens_with_sentiments, openai_api_key):
    """
    Generates a paragraph using GPT-3 based on provided tokens and their sentiment values.

    Args:
    tokens_with_sentiments (list of tuples): List of tuples where each tuple is (token, sentiment_value)
    openai_api_key (str): API key for accessing OpenAI's GPT-3

    Returns:
    str: A generated paragraph.
    """
    openai.api_key = openai_api_key

    # Constructing a refined prompt
    prompt = "Write a creative and coherent paragraph that includes the following words, respecting their associated sentiments:"
    logging.info(f"Prompt Supplied")
    for token, sentiment in tokens_with_sentiments:
        sentiment_desc = "positive" if sentiment > 0 else "negative" if sentiment < 0 else "neutral"
        prompt += f"\n- {token} ({sentiment_desc})"

    try:
        response = openai.Completion.create(engine="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=1000)
        logging.info(f"Prompt Processed")
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"
