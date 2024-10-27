# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 27, 2024 17:51:26
# Database: sqlite:////tmp/tmp.ehvW5zIh7b/thomasLogic_1/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Customer(SAFRSBaseX, Base):
    """
    description: Stores customer information including credit limits and balances.
    """
    __tablename__ = 'customers'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    credit_limit = Column(Float, nullable=False)
    balance = Column(Float)

    # parent relationships (access parent)

    # child relationships (access children)
    CustomerAddressList : Mapped[List["CustomerAddress"]] = relationship(back_populates="customer")
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")



class PaymentMethod(SAFRSBaseX, Base):
    """
    description: Stores payment methods available for customers.
    """
    __tablename__ = 'payment_methods'
    _s_collection_name = 'PaymentMethod'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)



class Product(SAFRSBaseX, Base):
    """
    description: Stores product details including unit prices.
    """
    __tablename__ = 'products'
    _s_collection_name = 'Product'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    unit_price = Column(Float, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    DiscountList : Mapped[List["Discount"]] = relationship(back_populates="product")
    ItemList : Mapped[List["Item"]] = relationship(back_populates="product")
    PurchaseOrderItemList : Mapped[List["PurchaseOrderItem"]] = relationship(back_populates="product")



class Shipper(SAFRSBaseX, Base):
    """
    description: Information about shipping companies.
    """
    __tablename__ = 'shippers'
    _s_collection_name = 'Shipper'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    ShipmentDetailList : Mapped[List["ShipmentDetail"]] = relationship(back_populates="shipper")



class Supplier(SAFRSBaseX, Base):
    """
    description: Information about suppliers who provide products.
    """
    __tablename__ = 'suppliers'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    PurchaseOrderList : Mapped[List["PurchaseOrder"]] = relationship(back_populates="supplier")



class CustomerAddress(SAFRSBaseX, Base):
    """
    description: Stores multiple addresses of a customer.
    """
    __tablename__ = 'customer_addresses'
    _s_collection_name = 'CustomerAddress'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    address = Column(String, nullable=False)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("CustomerAddressList"))

    # child relationships (access children)



class Discount(SAFRSBaseX, Base):
    """
    description: Contains information about discounts applicable to products.
    """
    __tablename__ = 'discounts'
    _s_collection_name = 'Discount'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('products.id'), nullable=False)
    discount_rate = Column(Float, nullable=False)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("DiscountList"))

    # child relationships (access children)



class Order(SAFRSBaseX, Base):
    """
    description: Stores order details including order date and notes.
    """
    __tablename__ = 'orders'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime)
    amount_total = Column(Float)
    date_shipped = Column(DateTime)
    notes = Column(String)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    ItemList : Mapped[List["Item"]] = relationship(back_populates="order")
    ShipmentDetailList : Mapped[List["ShipmentDetail"]] = relationship(back_populates="order")



class PurchaseOrder(SAFRSBaseX, Base):
    """
    description: Orders placed with suppliers to stock products.
    """
    __tablename__ = 'purchase_orders'
    _s_collection_name = 'PurchaseOrder'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    supplier_id = Column(ForeignKey('suppliers.id'), nullable=False)
    order_date = Column(DateTime)
    received = Column(Boolean)

    # parent relationships (access parent)
    supplier : Mapped["Supplier"] = relationship(back_populates=("PurchaseOrderList"))

    # child relationships (access children)
    PurchaseOrderItemList : Mapped[List["PurchaseOrderItem"]] = relationship(back_populates="purchase_order")



class Item(SAFRSBaseX, Base):
    """
    description: Details of items included in orders.
    """
    __tablename__ = 'items'
    _s_collection_name = 'Item'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('orders.id'), nullable=False)
    product_id = Column(ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    amount = Column(Float)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("ItemList"))
    product : Mapped["Product"] = relationship(back_populates=("ItemList"))

    # child relationships (access children)



class PurchaseOrderItem(SAFRSBaseX, Base):
    """
    description: Details of items ordered in purchase orders.
    """
    __tablename__ = 'purchase_order_items'
    _s_collection_name = 'PurchaseOrderItem'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    purchase_order_id = Column(ForeignKey('purchase_orders.id'), nullable=False)
    product_id = Column(ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("PurchaseOrderItemList"))
    purchase_order : Mapped["PurchaseOrder"] = relationship(back_populates=("PurchaseOrderItemList"))

    # child relationships (access children)



class ShipmentDetail(SAFRSBaseX, Base):
    """
    description: Details about shipments for orders.
    """
    __tablename__ = 'shipment_details'
    _s_collection_name = 'ShipmentDetail'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('orders.id'), nullable=False)
    shipper_id = Column(ForeignKey('shippers.id'), nullable=False)
    shipment_date = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("ShipmentDetailList"))
    shipper : Mapped["Shipper"] = relationship(back_populates=("ShipmentDetailList"))

    # child relationships (access children)
