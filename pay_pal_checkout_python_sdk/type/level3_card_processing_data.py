# coding: utf-8

"""
    Orders

    An order represents a payment between two or more parties. Use the Orders API to create, update, retrieve, authorize, and capture orders.

    The version of the OpenAPI document: 2.13
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from pay_pal_checkout_python_sdk.type.address_portable import AddressPortable
from pay_pal_checkout_python_sdk.type.line_item import LineItem
from pay_pal_checkout_python_sdk.type.money import Money

class RequiredLevel3CardProcessingData(TypedDict):
    pass

class OptionalLevel3CardProcessingData(TypedDict, total=False):
    shipping_amount: Money

    duty_amount: Money

    discount_amount: Money

    shipping_address: AddressPortable

    # Use this field to specify the postal code of the shipping location.
    ships_from_postal_code: str

    # A list of the items that were purchased with this payment. If your merchant account has been configured for Level 3 processing this field will be passed to the processor on your behalf.
    line_items: typing.List[LineItem]

class Level3CardProcessingData(RequiredLevel3CardProcessingData, OptionalLevel3CardProcessingData):
    pass
