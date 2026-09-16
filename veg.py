# Vegetable Market Mini Project
# Store: Venu Gopal Vegetables

# Inventory Data
veg = ['brinjal', 'tomato', 'onion']
quantity = [10.0, 20.0, 25.0]       # Available stock in kgs
cost_price = [45.0, 35.0, 40.0]     # Cost price per kg (for profit calculation)
price = [65.0, 50.0, 55.0]          # Selling price per kg
sold_qty = [0.0, 0.0, 0.0]          # Tracks quantities sold for reports

while True:
    print("\n" + "=" * 38)
    print("        VENU GOPAL VEGETABLES")
    print("=" * 38)
    print("1. Customer")
    print("2. Shopkeeper")
    print("3. Exit")
    print("=" * 38)
    
    role = input("Select role (1/2/3 or customer/shopkeeper/exit): ").strip().lower()

    # ------------------- 1. CUSTOMER INTERFACE -------------------
    if role in ('1', 'customer'):
        cart_items = []
        cart_qty = []
        cart_amt = []
        
        print("\n--- Welcome to Customer Counter ---")
        while True:
            # Display available stock & prices
            print("\nAvailable Vegetables:")
            print(f"{'Item':<12}{'Price/kg':<12}{'Available Stock':<15}")
            print("-" * 40)
            for i in range(len(veg)):
                print(f"{veg[i]:<12}Rs {price[i]:<9.2f}{quantity[i]:<6.1f} kg")
            print("-" * 40)
            
            item = input("\nWhat item do you want to buy (or type 'done' to finish): ").strip().lower()
            
            if item == 'done':
                if len(cart_items) > 0:
                    print("\nGenerating Bill...")
                    print("*" * 10, "VENU GOPAL VEGETABLES", "*" * 10)
                    print(f"{'Item':<12}{'Qty(kg)':<10}{'Price/kg':<10}{'Amount':<10}")
                    print("-" * 42)
                    total_bill = 0
                    for i in range(len(cart_items)):
                        c_item = cart_items[i]
                        c_qty = cart_qty[i]
                        c_amt = cart_amt[i]
                        unit_p = price[veg.index(c_item)]
                        print(f"{c_item:<12}{c_qty:<10.2f}Rs {unit_p:<8.2f}Rs {c_amt:<8.2f}")
                        total_bill += c_amt
                    print("-" * 42)
                    print(f"{'Total Bill Amount':<32}Rs {total_bill:.2f}")
                    print("*" * 43)
                    print("Thank you for shopping with us!\n")
                else:
                    print("No items were added to the cart.")
                break  # Exit customer shopping loop
            
            if item in veg:
                idx = veg.index(item)
                if quantity[idx] <= 0:
                    print(f"Sorry, {item} is out of stock!")
                    continue

                qty = float(input(f"How many kgs of {item} you want: "))

                if qty <= 0:
                    print("Quantity must be greater than 0.")
                elif qty <= quantity[idx]:
                    amt = price[idx] * qty
                    cart_items.append(item)
                    cart_qty.append(qty)
                    cart_amt.append(amt)
                    quantity[idx] -= qty
                    sold_qty[idx] += qty
                    print(f"Added {qty} kg of {item} to cart.")
                else:
                    print(f"Out of stock! Only {quantity[idx]} kg available.")
            else:
                print(f"Sorry, '{item}' is not available in our shop.")

    # ------------------- 2. SHOPKEEPER INTERFACE -------------------
    elif role in ('2', 'shopkeeper'):
        while True:
            print("\n--- Shopkeeper Dashboard ---")
            print("1. Add Vegetable")
            print("2. Delete Vegetable")
            print("3. Update Vegetable (Price / Quantity)")
            print("4. View Reports & Restock Suggestions")
            print("5. Back to Main Menu")
            
            choice = input("Enter choice (1-5): ").strip()
            
            # 2.1 Add Vegetable
            if choice == '1':
                new_item = input("Enter new vegetable name: ").strip().lower()
                if new_item in veg:
                    print("Vegetable already exists! Use Update to add more stock.")
                elif not new_item:
                    print("Name cannot be empty.")
                else:
                    new_qty = float(input("Enter initial quantity (kg): "))
                    new_cp = float(input("Enter cost price per kg: "))
                    new_sp = float(input("Enter selling price per kg: "))
                    veg.append(new_item)
                    quantity.append(new_qty)
                    cost_price.append(new_cp)
                    price.append(new_sp)
                    sold_qty.append(0.0)
                    print(f"'{new_item}' added successfully!")

            # 2.2 Delete Vegetable
            elif choice == '2':
                del_item = input("Enter vegetable name to delete: ").strip().lower()
                if del_item in veg:
                    idx = veg.index(del_item)
                    veg.pop(idx)
                    quantity.pop(idx)
                    cost_price.pop(idx)
                    price.pop(idx)
                    sold_qty.pop(idx)
                    print(f"'{del_item}' removed from the shop.")
                else:
                    print(f"'{del_item}' not found in inventory.")

            # 2.3 Update Vegetable
            elif choice == '3':
                up_item = input("Enter vegetable name to update: ").strip().lower()
                if up_item in veg:
                    idx = veg.index(up_item)
                    print(f"Current -> Stock: {quantity[idx]} kg | Cost Price: Rs {cost_price[idx]} | Selling Price: Rs {price[idx]}")
                    print("a. Add Stock (Quantity)")
                    print("b. Update Selling Price")
                    print("c. Update Cost Price")
                    sub_opt = input("Select update option (a/b/c): ").strip().lower()
                    
                    if sub_opt == 'a':
                        add_q = float(input("Enter additional quantity (kg): "))
                        quantity[idx] += add_q
                        print(f"Updated {up_item} stock: {quantity[idx]} kg")
                    elif sub_opt == 'b':
                        new_sp = float(input("Enter new selling price: "))
                        price[idx] = new_sp
                        print(f"Updated {up_item} selling price: Rs {price[idx]}")
                    elif sub_opt == 'c':
                        new_cp = float(input("Enter new cost price: "))
                        cost_price[idx] = new_cp
                        print(f"Updated {up_item} cost price: Rs {cost_price[idx]}")
                    else:
                        print("Invalid option selected.")
                else:
                    print(f"'{up_item}' not found.")

            # 2.4 Reports & Suggestions
            elif choice == '4':
                print("\n" + "=" * 50)
                print("           REPORTS & ANALYTICS")
                print("=" * 50)
                
                # Vegetables Inventory Report
                print("\n[1] VEGETABLES INVENTORY REPORT:")
                print(f"{'Item':<12}{'Available':<12}{'Cost Price':<12}{'Selling Price':<12}")
                print("-" * 50)
                for i in range(len(veg)):
                    print(f"{veg[i]:<12}{quantity[i]:<12.1f}Rs {cost_price[i]:<10.2f}Rs {price[i]:<10.2f}")
                
                # Revenue & Profit Calculation
                total_rev = 0
                total_cost = 0
                for i in range(len(veg)):
                    total_rev += sold_qty[i] * price[i]
                    total_cost += sold_qty[i] * cost_price[i]
                total_profit = total_rev - total_cost
                
                print("\n[2] REVENUE REPORT:")
                print(f"Total Revenue Generated : Rs {total_rev:.2f}")
                print(f"Total Cost of Goods Sold: Rs {total_cost:.2f}")
                print(f"Total Net Profit        : Rs {total_profit:.2f}")
                
                # Itemized Profit Report
                print("\n[3] ITEMIZED PROFIT REPORT:")
                print(f"{'Item':<12}{'Sold (kg)':<12}{'Revenue':<12}{'Profit':<12}")
                print("-" * 50)
                for i in range(len(veg)):
                    item_rev = sold_qty[i] * price[i]
                    item_profit = sold_qty[i] * (price[i] - cost_price[i])
                    print(f"{veg[i]:<12}{sold_qty[i]:<12.1f}Rs {item_rev:<10.2f}Rs {item_profit:<10.2f}")
                
                # Restock Suggestions
                print("\n[4] RESTOCK SUGGESTIONS:")
                low_stock_found = False
                for i in range(len(veg)):
                    if quantity[i] <= 5.0:
                        print(f"-> Alert: Stock is low for '{veg[i]}' (Only {quantity[i]:.1f} kg left). Get more {veg[i]} tomorrow!")
                        low_stock_found = True
                if not low_stock_found:
                    print("All vegetables have sufficient stock (> 5 kg).")
                print("=" * 50)

            elif choice == '5':
                break  # Back to main menu
            else:
                print("Invalid choice, please select 1 to 5.")

    # ------------------- 3. EXIT / CLOSE SHOP -------------------
    elif role in ('3', 'exit'):
        close = input("Do you want to close the shop? (yes/no): ").strip().lower()
        if close == 'yes':
            total_rev = 0
            total_cost = 0
            for i in range(len(veg)):
                total_rev += sold_qty[i] * price[i]
                total_cost += sold_qty[i] * cost_price[i]
            total_profit = total_rev - total_cost
            print("\n" + "*" * 10, "CLOSING SUMMARY", "*" * 10)
            print(f"Today's Total Revenue : Rs {total_rev:.2f}")
            print(f"Today's Total Profit  : Rs {total_profit:.2f}")
            print("Shop closed. Have a great day!")
            break
    else:
        print("Invalid role selected! Please choose 1, 2, or 3.")
