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
from pay_pal_checkout_python_sdk.type.name import Name
from pay_pal_checkout_python_sdk.type.shipping_option import ShippingOption

class RequiredShippingDetail(TypedDict):
    pass

class OptionalShippingDetail(TypedDict, total=False):
    name: Name

    # A classification for the method of purchase fulfillment (e.g shipping, in-store pickup, etc). Either `type` or `options` may be present, but not both.
    type: str

    # An array of shipping options that the payee or merchant offers to the payer to ship or pick up their items.
    options: typing.List[ShippingOption]

    address: AddressPortable

class ShippingDetail(RequiredShippingDetail, OptionalShippingDetail):
    pass
