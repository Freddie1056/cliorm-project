from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database and session
Base = declarative_base()
engine = create_engine('sqlite:///inventory.db')
Session = sessionmaker(bind=engine)

# Define the Item model
class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    category = Column(String)
    supplier = Column(String)

def init_db():
    Base.metadata.create_all(engine)

def get_session():
    return Session()

# Add item to the database
def add_item(name, price, quantity, category, supplier):
    session = get_session()
    item = Item(name=name, price=price, quantity=quantity, category=category, supplier=supplier)
    session.add(item)
    session.commit()
    print(f"Item {name} added successfully.")

# List all items
def list_items():
    session = get_session()
    items = session.query(Item).all()
    
    if items:
        print("ID | Name      | Price | Quantity | Category | Supplier")
        print("-" * 50)
        for item in items:
            print(f"{item.id}  | {item.name}  | {item.price}  | {item.quantity} | {item.category} | {item.supplier}")
    else:
        print("No items in the inventory.")

# Update item details
def update_item(item_id, new_name=None, new_price=None, new_quantity=None, new_category=None, new_supplier=None):
    session = get_session()
    item = session.query(Item).filter_by(id=item_id).first()
    
    if item:
        if new_name:
            item.name = new_name
        if new_price:
            item.price = new_price
        if new_quantity:
            item.quantity = new_quantity
        if new_category:
            item.category = new_category
        if new_supplier:
            item.supplier = new_supplier

        session.commit()
        print(f"Item {item_id} updated successfully.")
    else:
        print(f"Item with ID {item_id} not found.")

# Delete item from the database
def delete_item(item_id):
    session = get_session()
    item = session.query(Item).filter_by(id=item_id).first()
    
    if item:
        session.delete(item)
        session.commit()
        print(f"Item {item_id} deleted successfully.")
    else:
        print(f"Item with ID {item_id} not found.")
