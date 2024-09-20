from inventory.inventory import add_item, list_items, update_item, delete_item, init_db

def main():
    init_db()  # Ensure the database is set up

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. List Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            category = input("Enter category: ")
            supplier = input("Enter supplier: ")
            add_item(name, price, quantity, category, supplier)

        elif choice == '2':
            list_items()

        elif choice == '3':
            item_id = int(input("Enter the ID of the item to update: "))
            new_name = input("Enter new name (leave blank to keep unchanged): ")
            new_price = input("Enter new price (leave blank to keep unchanged): ")
            new_quantity = input("Enter new quantity (leave blank to keep unchanged): ")
            new_category = input("Enter new category (leave blank to keep unchanged): ")
            new_supplier = input("Enter new supplier (leave blank to keep unchanged): ")

            update_item(item_id, 
                        new_name or None, 
                        float(new_price) if new_price else None, 
                        int(new_quantity) if new_quantity else None, 
                        new_category or None, 
                        new_supplier or None)

        elif choice == '4':
            item_id = int(input("Enter the ID of the item to delete: "))
            delete_item(item_id)

        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
