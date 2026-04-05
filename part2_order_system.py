import copy

menu = {
    "Paneer Tikka": {"category": "Starters", "price": 180.0, "available": True},
    "Chicken Wings": {"category": "Starters", "price": 220.0, "available": False},
    "Veg Soup": {"category": "Starters", "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains", "price": 320.0, "available": True},
    "Dal Tadka": {"category": "Mains", "price": 180.0, "available": True},
    "Veg Biryani": {"category": "Mains", "price": 250.0, "available": True},
    "Garlic Naan": {"category": "Mains", "price": 40.0, "available": True},
    "Gulab Jamun": {"category": "Desserts", "price": 90.0, "available": True},
    "Rasgulla": {"category": "Desserts", "price": 80.0, "available": True},
    "Ice Cream": {"category": "Desserts", "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka": {"stock": 10, "reorder_level": 3},
    "Chicken Wings": {"stock": 8, "reorder_level": 2},
    "Veg Soup": {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka": {"stock": 20, "reorder_level": 5},
    "Veg Biryani": {"stock": 6, "reorder_level": 3},
    "Garlic Naan": {"stock": 30, "reorder_level": 10},
    "Gulab Jamun": {"stock": 5, "reorder_level": 2},
    "Rasgulla": {"stock": 4, "reorder_level": 3},
    "Ice Cream": {"stock": 7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1, "items": ["Paneer Tikka", "Garlic Naan"], "total": 220.0},
        {"order_id": 2, "items": ["Gulab Jamun", "Veg Soup"], "total": 210.0},
        {"order_id": 3, "items": ["Butter Chicken", "Garlic Naan"], "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4, "items": ["Dal Tadka", "Garlic Naan"], "total": 220.0},
        {"order_id": 5, "items": ["Veg Biryani", "Gulab Jamun"], "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
        {"order_id": 7, "items": ["Butter Chicken", "Veg Biryani"], "total": 570.0},
        {"order_id": 8, "items": ["Garlic Naan", "Gulab Jamun"], "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9, "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"], "total": 270.0},
    ],
}

# show menu

print("Menu list")

cats = []
for v in menu.values():
    if v["category"] not in cats:
        cats.append(v["category"])

for c in cats:
    print("\n", c)
    for name in menu:
        if menu[name]["category"] == c:
            d = menu[name]
            status = "yes" if d["available"] else "no"
            print(name, "- Rs.", d["price"], "-", status)

print("\nTotal items:", len(menu))

count = 0
for v in menu.values():
    if v["available"]:
        count += 1
print("Available:", count)

mx = max(menu, key=lambda x: menu[x]["price"])
print("Costliest:", mx, menu[mx]["price"])

print("\nUnder 150:")
for n in menu:
    if menu[n]["price"] < 150:
        print(n, menu[n]["price"])


# cart part

cart = []

def add_item(name, qty):
    if name not in menu:
        print("not in menu")
        return
    if not menu[name]["available"]:
        print("not available")
        return

    for i in cart:
        if i["item"] == name:
            i["qty"] += qty
            print("updated", name)
            return

    cart.append({"item": name, "qty": qty, "price": menu[name]["price"]})
    print("added", name)

def remove_item(name):
    for i in cart:
        if i["item"] == name:
            cart.remove(i)
            print("removed", name)
            return
    print("not found")

def show_cart():
    if not cart:
        print("empty cart")
    else:
        for i in cart:
            print(i["item"], "x", i["qty"], "@", i["price"])

print("\ncart demo")

add_item("Paneer Tikka", 2)
show_cart()

add_item("Gulab Jamun", 1)
show_cart()

add_item("Paneer Tikka", 1)
show_cart()

add_item("Mystery Burger", 1)
add_item("Chicken Wings", 1)

remove_item("Gulab Jamun")
show_cart()

print("\nBill")

sub = 0
for i in cart:
    t = i["qty"] * i["price"]
    sub += t
    print(i["item"], "=", t)

gst = round(sub * 0.05, 2)
total = sub + gst

print("Subtotal:", sub)
print("GST:", gst)
print("Total:", total)


# inventory part

print("\nInventory check")

backup = copy.deepcopy(inventory)

inventory["Paneer Tikka"]["stock"] = 999
print("changed stock:", inventory["Paneer Tikka"]["stock"])
print("backup stock:", backup["Paneer Tikka"]["stock"])

inventory["Paneer Tikka"]["stock"] = 10

for i in cart:
    item = i["item"]
    qty = i["qty"]

    if inventory[item]["stock"] >= qty:
        inventory[item]["stock"] -= qty
        print("used", item)
    else:
        print("low stock", item)
        inventory[item]["stock"] = 0

print("\nreorder check")
for i in inventory:
    if inventory[i]["stock"] <= inventory[i]["reorder_level"]:
        print(i, "low stock")


# sales part

print("\nSales info")

def show_sales(log):
    best = ""
    best_val = 0

    for d in log:
        total = 0
        for o in log[d]:
            total += o["total"]

        print(d, ":", total)

        if total > best_val:
            best_val = total
            best = d

    print("best day:", best)

show_sales(sales_log)

item_count = {}

for d in sales_log:
    for o in sales_log[d]:
        for it in o["items"]:
            if it in item_count:
                item_count[it] += 1
            else:
                item_count[it] = 1

top = max(item_count, key=lambda k: item_count[k])
print("top item:", top)

sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

print("\nafter adding new day")
show_sales(sales_log)

print("\nall orders")

c = 1
for d in sales_log:
    for o in sales_log[d]:
        print(c, d, o["order_id"], o["total"], o["items"])
        c += 1
