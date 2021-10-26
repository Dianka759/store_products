from store import Store
from products import Product

store = Store("the dojo store", ["toy", "food", "pet"])

kiwi = Product("Kiwi", 2000, "pet")
chicken = Product("chicken",20,"pet")
gummybears = Product("gummy bears", 1, "food")
plushie = Product("kitty cat", 50, "toy")

store.add_product(kiwi).add_product(chicken).add_product(gummybears).add_product(plushie)
print()

kiwi.print_info().update_price(.2, True).print_info()
print()
chicken.print_info().update_price(.2).print_info()


print()
store.sell_product(0)
store.sell_product(0)
store.sell_product(0)
store.sell_product(0)
