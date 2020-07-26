from quiq import F

def test_test():
    T = (F(1,4) == 2)
    assert T.function == 'F',    "Error with Tests.function"
    assert T.args     == [1,4], "Error with Tests.args"
    assert T.operator == '==',  "Error with Tests.operator"
    assert T.expected == 2,     "Error with Tests.expected"
