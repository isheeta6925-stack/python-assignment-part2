import copy

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}


# task 1 - print menu grouped by category

print("=" * 60)
print("TASK 1 - Full Menu by Category")
print("=" * 60)

cats = []
for item in menu.values():
    if item["category"] not in cats:
        cats.append(item["category"])

for cat in cats:
    print(f"\n===== {cat} =====")
    for name, details in menu.items():
        if details["category"] == cat:
            status = "[Available]" if details["available"] else "[Unavailable]"
            print(f"  {name:<18} Rs.{details['price']:.2f}   {status}")

total_items = len(menu)
available_count = sum(1 for d in menu.values() if d["available"])
priciest = max(menu, key=lambda x: menu[x]["price"])
budget_items = [(n, d["price"]) for n, d in menu.items() if d["price"] < 150]

print(f"\nTotal items on menu   : {total_items}")
print(f"Total available items : {available_count}")
print(f"Most expensive item   : {priciest} (Rs.{menu[priciest]['price']:.2f})")
print(f"\nItems priced under Rs.150:")
for name, price in budget_items:
    print(f"  {name} --- Rs.{price:.2f}")


# task 2 - cart

print("\n" + "=" * 60)
print("TASK 2 - Cart Operations")
print("=" * 60)

cart = []

def add_to_cart(item_name, quantity):
    if item_name not in menu:
        print(f"  '{item_name}' does not exist in the menu.")
        return
    if not menu[item_name]["available"]:
        print(f"  '{item_name}' is currently unavailable.")
        return
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] += quantity
            print(f"  Updated '{item_name}' quantity to {entry['quantity']}.")
            return
    cart.append({"item": item_name, "quantity": quantity, "price": menu[item_name]["price"]})
    print(f"  Added '{item_name}' x{quantity} to cart.")

def remove_from_cart(item_name):
    for entry in cart:
        if entry["item"] == item_name:
            cart.remove(entry)
            print(f"  Removed '{item_name}' from cart.")
            return
    print(f"  '{item_name}' is not in the cart.")

def print_cart():
    if not cart:
        print("  Cart is empty.")
    else:
        for entry in cart:
            print(f"    {entry['item']} x{entry['quantity']} @ Rs.{entry['price']:.2f}")

print("\n--- Adding Paneer Tikka x2 ---")
add_to_cart("Paneer Tikka", 2)
print_cart()

print("\n--- Adding Gulab Jamun x1 ---")
add_to_cart("Gulab Jamun", 1)
print_cart()

print("\n--- Adding Paneer Tikka x1 (quantity should update to 3) ---")
add_to_cart("Paneer Tikka", 1)
print_cart()

print("\n--- Trying to add Mystery Burger (does not exist) ---")
add_to_cart("Mystery Burger", 1)
print_cart()

print("\n--- Trying to add Chicken Wings (unavailable) ---")
add_to_cart("Chicken Wings", 1)
print_cart()

print("\n--- Removing Gulab Jamun ---")
remove_from_cart("Gulab Jamun")
print_cart()

print("\n========== Order Summary ==========")
subtotal = 0
for entry in cart:
    line_total = entry["quantity"] * entry["price"]
    subtotal += line_total
    print(f"  {entry['item']:<20} x{entry['quantity']}   Rs.{line_total:.2f}")

gst = round(subtotal * 0.05, 2)
total_payable = round(subtotal + gst, 2)
print("------------------------------------")
print(f"  Subtotal:                Rs.{subtotal:.2f}")
print(f"  GST (5%):                Rs.{gst:.2f}")
print(f"  Total Payable:           Rs.{total_payable:.2f}")
print("====================================")


# task 3 - inventory + deep copy

print("\n" + "=" * 60)
print("TASK 3 - Inventory Tracker with Deep Copy")
print("=" * 60)

inventory_backup = copy.deepcopy(inventory)

print("\nChanging Paneer Tikka stock to 999 in inventory to show deep copy works:")
inventory["Paneer Tikka"]["stock"] = 999
print(f"  inventory stock        = {inventory['Paneer Tikka']['stock']}")
print(f"  inventory_backup stock = {inventory_backup['Paneer Tikka']['stock']}")
print("  Backup is unaffected - deep copy confirmed!")

inventory["Paneer Tikka"]["stock"] = 10
print("\nInventory restored to original.")

print("\nFulfilling order from inventory:")
for entry in cart:
    item = entry["item"]
    qty = entry["quantity"]
    stock = inventory[item]["stock"]
    if stock >= qty:
        inventory[item]["stock"] -= qty
        print(f"  Deducted {qty} of '{item}'. Remaining stock: {inventory[item]['stock']}")
    else:
        print(f"  Not enough stock for '{item}'. Had {stock}, needed {qty}. Deducting {stock}.")
        inventory[item]["stock"] = 0

print("\n--- Reorder Alerts ---")
for item, data in inventory.items():
    if data["stock"] <= data["reorder_level"]:
        print(f"  Reorder Alert: {item} --- Only {data['stock']} unit(s) left (reorder level: {data['reorder_level']})")

print("\nCurrent inventory vs backup (Paneer Tikka):")
print(f"  inventory stock        : {inventory['Paneer Tikka']['stock']}")
print(f"  inventory_backup stock : {inventory_backup['Paneer Tikka']['stock']}")
print("  They differ - deep copy protected the original.")


# task 4 - sales log

print("\n" + "=" * 60)
print("TASK 4 - Daily Sales Log Analysis")
print("=" * 60)

def print_revenue_table(log):
    print(f"\n{'Date':<15} | {'Revenue':>10}")
    print("-" * 30)
    best_day = ""
    best_revenue = 0
    for date, orders in log.items():
        daily_rev = sum(order["total"] for order in orders)
        print(f"  {date:<13} | Rs.{daily_rev:>8.2f}")
        if daily_rev > best_revenue:
            best_revenue = daily_rev
            best_day = date
    print(f"\n  Best-selling day: {best_day} (Rs.{best_revenue:.2f})")

print_revenue_table(sales_log)

item_count = {}
for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:
            item_count[item] = item_count.get(item, 0) + 1

top_item = max(item_count, key=lambda x: item_count[x])
print(f"\nMost ordered item: {top_item} (appeared in {item_count[top_item]} orders)")

sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

print("\n--- Updated Revenue Table (after adding 2025-01-05) ---")
print_revenue_table(sales_log)

print("\n--- All Orders (Numbered) ---")
counter = 1
for date, orders in sales_log.items():
    for order in orders:
        items_str = ", ".join(order["items"])
        print(f"  {counter}. [{date}] Order #{order['order_id']}  --- Rs.{order['total']:.2f} --- Items: {items_str}")
        counter += 1