# Inventory Management System

## Overview

The **Inventory Management System** is a Python application designed to help users manage their inventory efficiently. It allows you to add items, view inventory, manage suppliers, and record transactions through a command-line interface.

## Features

- **Add Items**: Insert new items into the inventory with details such as name, price, and quantity.
- **View Inventory**: Display all items currently in stock.
- **Manage Suppliers**: Add and view supplier information.
- **Record Transactions**: Keep track of sales transactions.

## Getting Started

### Prerequisites

- **Python 3.x**: Ensure Python is installed on your machine.
- **SQLAlchemy**: Required for database interactions.

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/inventory_proj.git
   cd inventory_proj
Set up a Virtual Environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Running the Application
Activate the virtual environment (if not already):

bash
Copy code
source venv/bin/activate
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

