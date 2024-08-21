import cohere
from decouple import config
import random

def get_recipe(cuisines):
    """
Generates a recipe for a randomly selected cuisine from a given list of cuisines using the Cohere API.

Args:
    cuisines (list): A list of cuisine names (as strings) from which a random cuisine will be selected.

Returns:
    tuple: A tuple containing the generated recipe (str) and the selected cuisine (str).

Raises:
    Any exceptions raised by the Cohere API will propagate up.
"""

    selected_cuisine = random.choice(cuisines)
    COHERE_API_KEY = config('COHERE_API_KEY')


    cohere_client = cohere.Client(COHERE_API_KEY)


    prompt = (
        "You are a highly skilled chef specializing in various Indian cuisines. "
        "Your task is to provide a recipe for a randomly selected dish from a specific Indian cuisine. "
        "Ensure the recipe is detailed, including ingredients and steps.\n\n"
        f"Please provide a recipe for a dish from the following cuisine: {selected_cuisine}."
    )

    response = cohere_client.generate(
        prompt=prompt,

    )

    recipe = response.generations[0].text.strip()

    return recipe, selected_cuisine

