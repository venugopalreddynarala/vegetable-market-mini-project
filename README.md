# Vegetable Market Mini Project

## Venu Gopal Vegetables

A simple **Python-based Vegetable Market Management System** that manages vegetable inventory, customer purchases, billing, sales tracking, profit calculation, and restock suggestions.

## Features

### Customer Interface

* View available vegetables and prices
* Select vegetables to purchase
* Enter quantity in kilograms
* Automatically calculate item amounts
* Generate a customer bill
* Track sold quantity
* Automatically reduce available stock

### Shopkeeper Interface

* Add new vegetables
* Delete vegetables from inventory
* Add additional stock
* Update selling price
* Update cost price
* View inventory details
* View revenue and profit reports
* Get low-stock restock suggestions

### Reports & Analytics

The shopkeeper can view:

* Available stock
* Cost price
* Selling price
* Total revenue
* Total cost of goods sold
* Total net profit
* Item-wise quantity sold
* Item-wise revenue
* Item-wise profit
* Low-stock alerts

## Technologies Used

* Python
* Lists
* `while` loops
* `if-elif-else` conditions
* `for` loops
* User input
* Basic calculations

## Initial Inventory

| Vegetable | Quantity | Cost Price/kg | Selling Price/kg |
| --------- | -------: | ------------: | ---------------: |
| Brinjal   |    10 kg |           ₹45 |              ₹65 |
| Tomato    |    20 kg |           ₹35 |              ₹50 |
| Onion     |    25 kg |           ₹40 |              ₹55 |

## How to Run

Make sure Python is installed on your system.

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/vegetable-market-mini-project.git
```

Open the project folder:

```bash
cd vegetable-market-mini-project
```

Run the program:

```bash
python veg.py
```

## Main Menu

When the program starts, it provides three options:

```text
1. Customer
2. Shopkeeper
3. Exit
```

### Customer

Select `1` or type `customer` to enter the customer interface.

Customers can select vegetables, enter the required quantity, and generate a bill.

### Shopkeeper

Select `2` or type `shopkeeper` to open the shopkeeper dashboard.

The dashboard provides options to add, delete, and update vegetables and view reports.

### Exit

Select `3` or type `exit` to close the shop.

A closing summary displays the total revenue and total profit.

## Project Structure

```text
vegetable-market-mini-project/
│
├── veg.py
└── README.md
```

## Future Improvements

Possible improvements for future versions:

* Store inventory data permanently using a database
* Add a graphical user interface
* Add customer details and invoice numbers
* Save bills as PDF files
* Add daily, weekly, and monthly sales reports
* Add login authentication for shopkeepers
* Add date and time to transactions

## Author

**Venu Gopal Reddy**

Python Mini Project
Vegetable Market Management System
