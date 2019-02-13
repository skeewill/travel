from buses import possible, union

a = ['main', 'elm', 'maple', 'chestnut']
b = ['high', 'pine', 'elm', 'main', 'capital']
c = ['broad', 'oak', 'frank', 'pine']


def test_union():
    u = union(a, b)
    assert u == {'main', 'elm'}


def test_possible():
    res = possible(a, b, c)
    assert res == True
