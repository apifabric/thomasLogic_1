# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime, Table, Boolean
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

# Base Declarations
Base = declarative_base()

# Table: Customers
class Customer(Base):
    """
    description: Stores customer information including credit limits and balances.
    """
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    credit_limit = Column(Float, nullable=False)
    balance = Column(Float, default=0.0)

# Table: Orders
class Order(Base):
    """
    description: Stores order details including order date and notes.
    """
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.now)
    amount_total = Column(Float, default=0.0)
    date_shipped = Column(DateTime, nullable=True)
    notes = Column(String)

# Table: Items
class Item(Base):
    """
    description: Details of items included in orders.
    """
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    amount = Column(Float, default=0.0)

# Table: Products
class Product(Base):
    """
    description: Stores product details including unit prices.
    """
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    unit_price = Column(Float, nullable=False)

# Table: Customer Addresses
class CustomerAddress(Base):
    """
    description: Stores multiple addresses of a customer.
    """
    __tablename__ = 'customer_addresses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    address = Column(String, nullable=False)

# Table: Suppliers
class Supplier(Base):
    """
    description: Information about suppliers who provide products.
    """
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone = Column(String)

# Table: Purchase Orders
class PurchaseOrder(Base):
    """
    description: Orders placed with suppliers to stock products.
    """
    __tablename__ = 'purchase_orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.now)
    received = Column(Boolean, default=False)

# Table: Purchase Order Items
class PurchaseOrderItem(Base):
    """
    description: Details of items ordered in purchase orders.
    """
    __tablename__ = 'purchase_order_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    purchase_order_id = Column(Integer, ForeignKey('purchase_orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

# Table: Shippers
class Shipper(Base):
    """
    description: Information about shipping companies.
    """
    __tablename__ = 'shippers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)

# Table: Shipment Details
class ShipmentDetail(Base):
    """
    description: Details about shipments for orders.
    """
    __tablename__ = 'shipment_details'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    shipper_id = Column(Integer, ForeignKey('shippers.id'), nullable=False)
    shipment_date = Column(DateTime, nullable=False)

# Table: Discounts
class Discount(Base):
    """
    description: Contains information about discounts applicable to products.
    """
    __tablename__ = 'discounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    discount_rate = Column(Float, nullable=False)

# Table: Payment Methods
class PaymentMethod(Base):
    """
    description: Stores payment methods available for customers.
    """
    __tablename__ = 'payment_methods'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

# Setup function to create the database and populate sample data
def setup_database():
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Sample Data Insertion
    # Create some sample products
    product1 = Product(name="Widget", unit_price=10.0)
    product2 = Product(name="Gadget", unit_price=20.0)
    session.add_all([product1, product2])
    
    # Create some sample customers
    customer1 = Customer(name="John Doe", credit_limit=100.0)
    customer2 = Customer(name="Jane Smith", credit_limit=200.0)
    session.add_all([customer1, customer2])
    
    # Create a sample order
    order1 = Order(customer_id=1, notes="Urgent order")
    order2 = Order(customer_id=2, notes="Regular shipment")
    session.add_all([order1, order2])
    
    # Create some items for the orders
    item1 = Item(order_id=1, product_id=1, quantity=2, unit_price=10.0, amount=20.0)
    item2 = Item(order_id=2, product_id=2, quantity=3, unit_price=20.0, amount=60.0)
    session.add_all([item1, item2])
    
    # Create sample supplier
    supplier1 = Supplier(name="SupplyCo", phone="555-1234")
    supplier2 = Supplier(name="GoodsRUs", phone="555-5678")
    session.add_all([supplier1, supplier2])
    
    # Create sample shipper
    shipper1 = Shipper(name="FastShip", contact_info="fastship@example.com")
    shipper2 = Shipper(name="QuickSend", contact_info="quicksend@example.com")
    session.add_all([shipper1, shipper2])
    
    # Create sample purchase orders
    purchase_order1 = PurchaseOrder(supplier_id=1)
    purchase_order2 = PurchaseOrder(supplier_id=2)
    session.add_all([purchase_order1, purchase_order2])
    
    # Create sample purchase order items
    purchase_order_item1 = PurchaseOrderItem(purchase_order_id=1, product_id=1, quantity=10)
    purchase_order_item2 = PurchaseOrderItem(purchase_order_id=2, product_id=2, quantity=5)
    session.add_all([purchase_order_item1, purchase_order_item2])

    # Create sample customer addresses
    address1 = CustomerAddress(customer_id=1, address="123 Elm Street")
    address2 = CustomerAddress(customer_id=2, address="456 Oak Avenue")
    session.add_all([address1, address2])
    
    # Create sample shipment details
    shipment_detail1 = ShipmentDetail(order_id=1, shipper_id=1, shipment_date=datetime.now())
    shipment_detail2 = ShipmentDetail(order_id=2, shipper_id=2, shipment_date=datetime.now())
    session.add_all([shipment_detail1, shipment_detail2])
    
    # Create sample discount
    discount1 = Discount(product_id=1, discount_rate=0.1)
    discount2 = Discount(product_id=2, discount_rate=0.2)
    session.add_all([discount1, discount2])
    
    # Create sample payment method
    payment_method1 = PaymentMethod(name="Credit Card")
    payment_method2 = PaymentMethod(name="PayPal")
    session.add_all([payment_method1, payment_method2])

    session.commit()
    session.close()

# Execute setup
setup_database()

# LogicBank Rule Declaration
def declare_logic():
    Rule.sum(derive=Customer.balance, as_sum_of=Order.amount_total, where=lambda row: row.date_shipped is None)
    Rule.sum(derive=Order.amount_total, as_sum_of=Item.amount)
    Rule.formula(derive=Item.amount, as_expression=lambda row: row.quantity * row.unit_price)
    Rule.copy(derive=Item.unit_price, from_parent=Product.unit_price)
    Rule.constraint(validate=Customer,
                    as_condition=lambda row: row.balance <= row.credit_limit,
                    error_msg="Customer balance ({row.balance}) exceeds credit limit ({row.credit_limit})")

