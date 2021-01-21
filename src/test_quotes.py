# Import des ressources
import pytest
from quotes import random_quote
from random import randint

# Test du tirage d'une citation
def test_random_quote() -> None:
    # On tire une douzaine de quotes et check chacune d'entre elle
    for i in range(12):
        quote = random_quote()
        assert(quote.text and quote.author)

def test_random_quote_author() -> None:
    # On tire une douzaine de quotes avec un auteur et check chacune d'entre elle
    for i in range(12):
        quote = random_quote(["Vincent V.K.", "Stefano S.", "Claire T.B.", "Jean-Caude Van Dam"][randint(0, 3)])
        assert(quote.text and quote.author)