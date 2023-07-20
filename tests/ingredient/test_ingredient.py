from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingrediente = Ingredient("ovo")

    assert ingrediente.__repr__() == "Ingredient('ovo')"
    assert ingrediente.__hash__() == hash("ovo")
    assert ingrediente.name == "ovo"
    assert ingrediente.restrictions
    assert ingrediente != 'oi'
    assert ingrediente != "ovo"
    assert ingrediente == Ingredient("ovo")
