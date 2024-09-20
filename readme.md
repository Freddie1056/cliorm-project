# Inventory Management System

A robust **Inventory Management System** built with Python and SQLAlchemy, designed to effectively manage stock. This CLI application allows users to add items, view inventory, manage suppliers, and record transactions.

## Features

- **Add New Items**: Insert new inventory items with details like name, price, and quantity.
- **View Inventory**: List all items currently in stock along with their respective details.
- **Manage Suppliers**: Add and view supplier information.
- **Record Transactions**: Keep track of sales transactions associated with inventory items.

## Getting Started

To set up the Inventory Management System on your local machine, follow these steps:

### Prerequisites

Ensure you have the following installed:

- **Python 3.x**: [Download from python.org](https://www.python.org/downloads/).
- **Pipenv**: Use `pip install pipenv` to install if not already available.

### Set Up a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate

Install Dependencies
bash
Copy code
pip install -r requirements.txt
Run the main program:

bash
Copy code
python main.py
Usage
Follow the prompts in the command line to add items, view inventory, manage suppliers, and record transactions.

Example Commands
To add an item, you might enter:

yaml
Copy code
Enter item name: Laptop
Enter item price: 1500
Enter item quantity: 10
To view the inventory, simply follow the prompts.

Database Structure
The application uses SQLAlchemy to manage a SQLite database (inventory.db) with the following tables:

items: Stores item details (id, name, price, quantity, supplier_id).
suppliers: Stores supplier information (id, name, contact_info).
transactions: Records sales transactions (id, item_id, quantity_sold, transaction_date).
License
This project is licensed under the MIT License. For more details, refer to the LICENSE file.

Repository
You can clone the project from here.