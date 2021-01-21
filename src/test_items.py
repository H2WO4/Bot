# Import des ressources
import pytest
from item_chest import generateItem

# Test du tirage d'une douzaine d'items
def test_generateItem() -> None:
    # On tire 12 quotes et check chacune d'entre elle
    for i in range(12):
        item = generateItem()

        assert(item[0] and item[1])