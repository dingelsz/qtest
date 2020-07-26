from qtest import test_case

def test_test_case():
    @TestCase(
        F(6, 5).isin(list(range(2,50))),
        F(6, 5) == 11,
        F(1,2) == 51,
        F(1,2).throws()
    )
    def add(x, y):
        if x == 1: raise ValueError("No 1s!")
        return x + y
