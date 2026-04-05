Bitsom_ba_2511354_Srivastava_Isheeta_Python-Assignment-Part2-OUTPUT

PS C:\Users\Isheeta> & C:/Users/Isheeta/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/assignment/python-assignment-part2/python-assignment-part2/part2_order_system.py
============================================================
TASK 1 - Full Menu by Category
============================================================

===== Starters =====
  Paneer Tikka       Rs.180.00   [Available]
  Chicken Wings      Rs.220.00   [Unavailable]
  Veg Soup           Rs.120.00   [Available]

===== Mains =====
  Butter Chicken     Rs.320.00   [Available]
  Dal Tadka          Rs.180.00   [Available]
  Veg Biryani        Rs.250.00   [Available]
  Garlic Naan        Rs.40.00   [Available]

===== Desserts =====
  Gulab Jamun        Rs.90.00   [Available]
  Rasgulla           Rs.80.00   [Available]
  Ice Cream          Rs.110.00   [Unavailable]

Total items on menu   : 10
Total available items : 8
Most expensive item   : Butter Chicken (Rs.320.00)

Items priced under Rs.150:
  Veg Soup --- Rs.120.00
  Garlic Naan --- Rs.40.00
  Gulab Jamun --- Rs.90.00
  Rasgulla --- Rs.80.00
  Ice Cream --- Rs.110.00

============================================================
TASK 2 - Cart Operations
============================================================

--- Adding Paneer Tikka x2 ---
  Added 'Paneer Tikka' x2 to cart.
    Paneer Tikka x2 @ Rs.180.00

--- Adding Gulab Jamun x1 ---
  Added 'Gulab Jamun' x1 to cart.
    Paneer Tikka x2 @ Rs.180.00
    Gulab Jamun x1 @ Rs.90.00

--- Adding Paneer Tikka x1 (quantity should update to 3) ---
  Updated 'Paneer Tikka' quantity to 3.
    Paneer Tikka x3 @ Rs.180.00
    Gulab Jamun x1 @ Rs.90.00

--- Trying to add Mystery Burger (does not exist) ---
  'Mystery Burger' does not exist in the menu.
    Paneer Tikka x3 @ Rs.180.00
    Gulab Jamun x1 @ Rs.90.00

--- Trying to add Chicken Wings (unavailable) ---
  'Chicken Wings' is currently unavailable.
    Paneer Tikka x3 @ Rs.180.00
    Gulab Jamun x1 @ Rs.90.00

--- Removing Gulab Jamun ---
  Removed 'Gulab Jamun' from cart.
    Paneer Tikka x3 @ Rs.180.00

========== Order Summary ==========
  Paneer Tikka         x3   Rs.540.00
------------------------------------
  Subtotal:                Rs.540.00
  GST (5%):                Rs.27.00
  Total Payable:           Rs.567.00
====================================

============================================================
TASK 3 - Inventory Tracker with Deep Copy
============================================================

Changing Paneer Tikka stock to 999 in inventory to show deep copy works:
  inventory stock        = 999
  inventory_backup stock = 10
  Backup is unaffected - deep copy confirmed!

Inventory restored to original.

Fulfilling order from inventory:
  Deducted 3 of 'Paneer Tikka'. Remaining stock: 7

--- Reorder Alerts ---

Current inventory vs backup (Paneer Tikka):
  inventory stock        : 7
  inventory_backup stock : 10
  They differ - deep copy protected the original.

============================================================
TASK 4 - Daily Sales Log Analysis
============================================================

Date            |    Revenue
------------------------------
  2025-01-01    | Rs.  790.00
  2025-01-02    | Rs.  560.00
  2025-01-03    | Rs.  960.00
  2025-01-04    | Rs.  570.00

  Best-selling day: 2025-01-03 (Rs.960.00)

Most ordered item: Garlic Naan (appeared in 5 orders)

--- Updated Revenue Table (after adding 2025-01-05) ---

Date            |    Revenue
------------------------------
  2025-01-01    | Rs.  790.00
  2025-01-02    | Rs.  560.00
  2025-01-03    | Rs.  960.00
  2025-01-04    | Rs.  570.00
  2025-01-05    | Rs.  750.00

  Best-selling day: 2025-01-03 (Rs.960.00)

--- All Orders (Numbered) ---
  1. [2025-01-01] Order #1  --- Rs.220.00 --- Items: Paneer Tikka, Garlic Naan
  2. [2025-01-01] Order #2  --- Rs.210.00 --- Items: Gulab Jamun, Veg Soup
  3. [2025-01-01] Order #3  --- Rs.360.00 --- Items: Butter Chicken, Garlic Naan
  4. [2025-01-02] Order #4  --- Rs.220.00 --- Items: Dal Tadka, Garlic Naan
  5. [2025-01-02] Order #5  --- Rs.340.00 --- Items: Veg Biryani, Gulab Jamun
  6. [2025-01-03] Order #6  --- Rs.260.00 --- Items: Paneer Tikka, Rasgulla
  7. [2025-01-03] Order #7  --- Rs.570.00 --- Items: Butter Chicken, Veg Biryani
  8. [2025-01-03] Order #8  --- Rs.130.00 --- Items: Garlic Naan, Gulab Jamun
  9. [2025-01-04] Order #9  --- Rs.300.00 --- Items: Dal Tadka, Garlic Naan, Rasgulla
  10. [2025-01-04] Order #10  --- Rs.270.00 --- Items: Paneer Tikka, Gulab Jamun
  11. [2025-01-05] Order #11  --- Rs.490.00 --- Items: Butter Chicken, Gulab Jamun, Garlic Naan
  12. [2025-01-05] Order #12  --- Rs.260.00 --- Items: Paneer Tikka, Rasgulla
PS C:\Users\Isheeta> 
