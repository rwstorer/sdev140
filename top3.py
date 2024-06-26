# request an item
# request an item price
# print the item and the price

items: dict = {'item2': 2.53, 'item1': 1.25, 'item3': 0.75}
item_list: list = [0.75, 2.53, 1.25]

item_list.sort(reverse=True)
print(item_list)

for key in items.keys():
    print(f"{key} {items[key]}")