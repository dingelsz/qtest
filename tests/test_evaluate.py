from qtest.evaluate import evaluate

def test_evaluate():
    assert evaluate(['car', ['list', 1, 2, 3]])	== 1, "Error with car/list"
    assert evaluate(['cdr', ['list', 1, 2, 3]])	== [2,3], "Error with cdr/list"
    assert evaluate(['==', 1, 1])                   == True, "Error with =="
    assert evaluate(['!=', 1, 2])			== True, "Error with !="
    assert evaluate(['isin', 1, ['list',1,2,3]])	== True, "Error with isin"
    assert evaluate(['isin', 4, ['list',1,2,3]])	== False, "Error with isin"
    assert evaluate(['quote', [4, ['list',1,2,3]]]) == [4, ['list', 1, 2, 3]], "Error with quote"
