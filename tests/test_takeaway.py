from lib.takeaway import *

def test_initialised_correctly():
    menu = {"fish":5.9, "chicken":7.8}
    takeaway = Takeaway(menu)
    assert takeaway.view_dishes() == menu
    assert takeaway.order == []

def test_add_dish():
    menu = {"fish":5.9, "chicken":7.8}
    takeaway = Takeaway(menu)
    takeaway.add_dish("chicken")
    takeaway.add_dish("fish")
    takeaway.add_dish(("chicken"))
    assert takeaway.order == ["chicken", "fish", "chicken"]

def test_calculate_receipt():
    menu = {"fish":5.9, "chicken":7.8}
    takeaway = Takeaway(menu)
    takeaway.add_dish("chicken")
    takeaway.add_dish("fish")
    takeaway.add_dish(("chicken"))
    assert takeaway.calculate_receipt() == [21.5, ["chicken", "fish", "chicken"]]
    